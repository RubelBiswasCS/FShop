from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2081)


class Offer(models.Model):
    code = models.CharField(max_length=100)
    descriptions = models.CharField(max_length=300)
    discount = models.FloatField()

