from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

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

    def __str__(self): return self.title

