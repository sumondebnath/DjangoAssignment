from django.db import models
from brands.models import Brands

# Create your models here.
class Cars(models.Model):
    car_name = models.CharField(max_length=50)
    car_price = models.CharField(max_length=15)
    car_discription = models.TextField()
    quentities = models.IntegerField()
    car_image = models.ImageField(upload_to="cars/media/post/", null=True, blank=True)

    brand = models.ForeignKey(Brands, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_name
    

class Comment(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name="comment", )
    name = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    def __str__(self):
        return f"Comments By: {self.name}"