from django import forms
from cars.models import Comment

class commentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["name", "body"]