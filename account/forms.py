from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.forms import PasswordChangeForm


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    terms_checkbox = forms.BooleanField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email.endswith('@acg.edu'):
            raise ValidationError("Email must end with @acg.edu")
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        return username

class UserInfo(models.Model):
    phone_number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.UserInfo
class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput
    )
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})

        