from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=1000)
    price = models.CharField(max_length=10000)
    currency = models.CharField(max_length=20)
    image_url = models.CharField(max_length=10000)
    created = models.DateTimeField(auto_now_add=True)