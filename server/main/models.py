from django.db import models


class Order(models.Model):
    status = models.CharField(max_length=255)
    tinkID = models.CharField(max_length=255)
    amount = models.IntegerField()
    userId = models.CharField(max_length=255)
    comment = models.TextField(default="")
    
    created_date = models.DateTimeField(auto_now_add=True)
    readies_date = models.DateTimeField(null=True)

    def __str__(self) -> str:
        return f"{self.id}:{self.status}:{self.tinkID}"


class OrderItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.IntegerField()

    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Log(models.Model):
    url = models.URLField()
    requests_date = models.DateTimeField(auto_now_add=True)
    headers = models.TextField()
    body = models.TextField()


class Category(models.Model):
    name = models.CharField(max_length=255)
    hash = models.CharField(max_length=255)

    def __str__(self): return self.name


class Product(models.Model):
    path = models.CharField(max_length=255)
    weight = models.IntegerField()
    title = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    compound = models.TextField()
    price = models.IntegerField()
    isVisible = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self): 
        return self.title

