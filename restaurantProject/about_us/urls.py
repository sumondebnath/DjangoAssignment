
from django.urls import path
from . import views

urlpatterns = [
    path("about/<int:id>/", views.about, name="about-us"),
]