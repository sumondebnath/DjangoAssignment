from django.shortcuts import render, redirect
from category.forms import categoryForm

# Create your views here.
def addCategory(request):
    if request.method == "POST":
        form = categoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("add_category")
    else:
        form = categoryForm()
    return render(request, "category/addcategory.html", {"form":form})