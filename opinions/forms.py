from django import forms
from .models import ProfessorPost,Professor

class ProfessorForm(forms.ModelForm):#I create a form to create professors
    class Meta:
        model = Professor
        fields = ['name'] #just the name is enough for adding a new professor


class ProfessorPostForm(forms.ModelForm):
    class Meta:
        model = ProfessorPost #I specify which models this form is based on
        fields = ['content'] # for when you add a comment about a professor 