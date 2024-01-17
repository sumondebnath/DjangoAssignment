from django.urls import path
from user import views

urlpatterns = [
    path("signup/", views.SignUp, name="sign_up"),
    path("login/", views.LogIn.as_view(), name="log_in"),
    path("edit-profile/", views.editProfile, name="editprofile"),
    path("profile/", views.Profile, name="profile"),
    path("logout/", views.LogOut.as_view(), name="log_out"),
]