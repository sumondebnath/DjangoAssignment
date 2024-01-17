from django.shortcuts import render, redirect
from user import forms, models
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

def SignUp(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("log_in")
    else:
        form = forms.UserForm()
    return render(request, "register.html", {"form":form, "type":"SIGN UP"})

class LogIn(LoginView):
    template_name = "register.html"

    def form_valid(self, form):
        return super().form_valid(form)
    def form_invalid(self, form):
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type"] = "LOG IN"
        return context
    def get_success_url(self):
        return reverse_lazy("home")
    
class LogOut(LogoutView):
    def get_success_url(self):
        return reverse_lazy("log_in")
    
@login_required
def Profile(request):
    return render(request, "profile.html")

@login_required
def editProfile(request):
    if request.method == "POST":
        form = forms.UserForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = forms.UserForm(instance=request.user)
    return render(request, "register.html", {"form":form, "type":"Edit Profile"})        