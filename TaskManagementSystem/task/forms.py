from django import forms
from task.models import Task

class taskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"