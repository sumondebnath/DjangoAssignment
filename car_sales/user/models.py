from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class store(models.Model):
    car_name = models.CharField(max_length=50)
    car_price = models.CharField(max_length=15)
    car_image = models.ImageField(upload_to="cars/media/post/", null=True, blank=True)
    brand_name = models.CharField(max_length = 50)

    user = models.ForeignKey(User, on_delete=models.CASCADE)