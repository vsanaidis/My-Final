from django import forms
from .models import Post, Comment,PostImage

# I created this form for the users to be able to create a post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description']
#This post I created is for the comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
from django import forms
from .models import Post, PostImage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description']
#form for creating (posting) an image( note )
class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']

PostImageFormSet = forms.inlineformset_factory(Post, PostImage, form=PostImageForm, extra=3)
