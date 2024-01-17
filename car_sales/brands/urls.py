from django.urls import path
from brands import views

urlpatterns = [
    path("brand/", views.brand),
]