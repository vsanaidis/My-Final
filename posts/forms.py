from django import forms
from .models import Post, Comment,PostImage


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['description']

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

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']

PostImageFormSet = forms.inlineformset_factory(Post, PostImage, form=PostImageForm, extra=3)
