from django import forms
from django.core.exceptions import ValidationError
from .models import Post

class NewsForm(forms.ModelForm):
    text = forms.CharField(min_length=20)
    class Meta:
        model = Post
        fields = ['author', 'postCategory', 'title', 'text', 'rating']
