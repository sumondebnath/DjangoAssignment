from django.shortcuts import render, redirect
from brands.models import Brands
from cars.models import Cars, Comment
from django.views.generic import DetailView
from cars.forms import commentForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def home(request, brand_slug = None):
    cars = Cars.objects.all()
    if brand_slug is not None:
        brand = Brands.objects.get(slug = brand_slug)
        cars = Cars.objects.filter(brand = brand)
    data = Brands.objects.all()
    return render(request, "home.html", {"cars":cars, "data":data})

@login_required
def Buy(request, id):
    data = Cars.objects.get(pk = id)
    if data.quentities > 0:
        data.quentities -= 1
    data.save()
    print(data.quentities)
    return render(request, "profile.html", {"data": data})


class Details(DetailView):
    model = Cars
    pk_url_kwarg = "id"
    template_name = "details.html"

    def post(self, request, *args, **kwargs):
        comment_form =  commentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        comments = post.comment.all()
        comment_form = commentForm()
        
        context["comments"] = comments
        context["comment_form"] = comment_form
        return context
