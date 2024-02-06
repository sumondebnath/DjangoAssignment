from django.db import models

# Create your models here.
class Task(models.Model):
    taskTitle = models.CharField(max_length=100)
    taskDescription = models.TextField()
    isCompleted = models.BooleanField(default=False)
    TaskAssignDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.taskTitle