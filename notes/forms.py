from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post  # Assuming you're creating a post
        fields = ['note', 'description', 'image']  # Adjust fields as needed
