from django.db import models
from django.utils import timezone
from PIL import Image
# Create your models here.
class Menu(models.Model):
    food_name = models.CharField(max_length=50)
    food_price = models.FloatField(default=5.0)
    food_desc = models.CharField(default="Yemek", max_length=150)
    food_image = models.ImageField(upload_to="food_pics", default="default.jpg")

    def __str__(self):
        return self.food_name

class Order(models.Model):
    orderer_name = models.CharField(max_length=100)
    orderer_surname = models.CharField(max_length=100)
    orderer_email = models.EmailField()
    orderer_phone = models.CharField(max_length=11)
    orderer_address = models.CharField(max_length=200)
    order_price = models.FloatField()
    order_detail = models.TextField(null=True)

    def __str__(self):
        return self.order_detail