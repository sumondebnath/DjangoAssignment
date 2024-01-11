from django.urls import path
from category.views import addCategory

urlpatterns = [
    path("add/category/", addCategory, name="add_category"),
]