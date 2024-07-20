from django import forms
from .models import ProfessorPost,Professor

class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = ['name']


class ProfessorPostForm(forms.ModelForm):
    class Meta:
        model = ProfessorPost
        fields = ['content']