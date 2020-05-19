from django.db import models
from django.utils import timezone
from PIL import Image
# Create your models here.
class Menu(models.Model):
    food_name = models.CharField(max_length=200)
    food_price = models.FloatField(default=5.0)
    food_desc = models.TextField(default="Yemek")
    food_image = models.ImageField(upload_to="food_pics", default="default.jpg")

