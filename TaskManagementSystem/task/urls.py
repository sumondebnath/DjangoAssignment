from django.urls import path
from task.views import addTask, showTask, editTask, deleteTask

urlpatterns = [
    path("add/task/", addTask, name="add_task"),
    path("show/task/", showTask, name="show_task"),
    path("edit/task/<int:id>", editTask, name="edit_task"),
    path("delete/task/<int:id>", deleteTask, name="delete_task")
]