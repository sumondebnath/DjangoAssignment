from django.urls import path
from cars import views

urlpatterns = [
    path("car/", views.car),
]