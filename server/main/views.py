from rest_framework import viewsets
from rest_framework.views import APIView
from django.shortcuts import redirect

from .models import Category, Product, Order, OrderItem
from .serializer import CategorySerializer, ProductSerializer, OrderSerializer
from rest_framework.response import Response

import telebot
import json

API_TOKEN = '7107976356:AAELWm4P1Nb2sK2yEueUpBXBFSX4JOjDllU'
bot = telebot.TeleBot(token=API_TOKEN)


class CreateOrderView(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        orderSerializer = OrderSerializer(data = {
            "status": "created", 
            "tinkID": data.get("OrderId"),
            "amount": data.get("Amount"),
            "userId": data.get("userId"),
            "comment": str(data.get("OrderData")),
        })

        if orderSerializer.is_valid(): 
            order = orderSerializer.save()

            for item in data.get("Receipt").get("Items"):
                orderItem = OrderItem.objects.create(
                    name=item.get("Name"),
                    quantity=item.get("Quantity"),
                    price=item.get("Price"),
                    order=order
                )

            orderItem.save()

            orderItems = OrderItem.objects.filter(order_id=order.id)
            print([item.name for item in orderItems])

            order_info = f"Информация о заказе №{order.id}\n\n"

            for index, item in enumerate(orderItems):
                order_info += f"{index+1}. {item.name} {item.quantity}шт.\n" 


            bot.send_message(
                order.userId,
                order_info
            )

            return Response({'message': 'Order created successfully'})
        
        return Response(orderSerializer.errors, status=400)
        

class SuccesPaymentView(APIView):
    async def post(self, request, *args, **kwargs):
        data = json.loads(request.body)

        order = Order.objects.get(tinkID=data.get("OrderId"))
        order.status = 'paid'
        order.save()

        bot.send_message(
            int(order.userId),
            "Order created successfully" 
        )

        return redirect(f"https://poco-loco.netlify.app/{order.userId}")


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
