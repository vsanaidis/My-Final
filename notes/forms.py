from django import forms
from .models import Post
#a simple form to create an add post for the users
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['note', 'description', 'image']  
