from django.shortcuts import render

# Create your views here.

def about(request, id):

    return render(request, "about_us/about.html", {"id":id})