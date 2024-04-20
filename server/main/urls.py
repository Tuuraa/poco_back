from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CategoryViewSet, ProductViewSet, SuccesPaymentView, CreateOrderView


router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("create_order/", CreateOrderView.as_view()),
    path("succes_payment/", SuccesPaymentView.as_view()),
    path('api/', include(router.urls)),
]