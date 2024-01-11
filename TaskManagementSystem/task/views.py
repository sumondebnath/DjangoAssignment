from django.shortcuts import render, redirect
from task.forms import taskForm
from task.models import Task
from category.models import Category

# Create your views here.
def addTask(request):
    if request.method == "POST":
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
            # print(request.POST)
            return redirect("add_task")
    else:
        form = taskForm()
    return render(request, "task/addtask.html", {"form":form})

def showTask(request):
    datas = Category.objects.all()
    return render(request, "task/showtask.html", {"datas":datas})

def editTask(request, id):
    data = Task.objects.get(pk=id)
    form = taskForm(instance=data)

    if request.method == "POST":
        form = taskForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("show_task")
    return render(request, "task/addtask.html", {"form":form})

def deleteTask(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return redirect("show_task")