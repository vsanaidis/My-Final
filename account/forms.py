from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile

# signup form for use registration, all input is required
class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=15, required=True)
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    terms_checkbox = forms.BooleanField(required=True)

    class Meta:
        model = get_user_model() #Here I am getting the user model
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2') #the fields displayed in the registration

    def clean_email(self): #custom email validation form
        email = self.cleaned_data.get('email') 
        if not email.endswith('@acg.edu'):#here I am ensuring that the user's email ends with acg.edu, it is for specific users.
            raise ValidationError("Email must end with @acg.edu") 
        return email

    def clean_username(self): #custom username method for more validation when needed (later updates)
        username = self.cleaned_data.get('username')
        return username
#class for more information that is the user's phone number (later updates)
class UserInfo(models.Model):
    phone_number = models.CharField(max_length=15, unique=True) #stores the user's phone number as CharField.

    def __str__(self):
        return self.UserInfo #returns the phonenumber 
    
#the class for login form, for when the user is logging in   
class LoginForm(forms.Form):
    username = forms.CharField(max_length=15, required=True)
    password = forms.CharField(
        widget=forms.PasswordInput
    )

#my custom password change form which takes the built-in django form and adds more to it 
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.core.exceptions import ValidationError

class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Current Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )
    new_password1 = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        help_text="Your password must contain at least 8 characters, including letters and numbers."
    )
    new_password2 = forms.CharField(
        label="Confirm New Password",
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )

    def clean_new_password1(self):
        password = self.cleaned_data.get('new_password1')
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one number.")
        if not any(char.isalpha() for char in password):
            raise ValidationError("Password must contain at least one letter.")
        return password
        
class UserUpdateForm(forms.ModelForm):

    email = models.EmailField()

    class Meta:

        model = User  
        fields = ['first_name','last_name','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']