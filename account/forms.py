from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.forms import PasswordChangeForm

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
class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):# I used the *args and *kwargs to pass arguments to the parent class and help with the handling of variable number of arguments.
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control'}) #here I add classes to the forms for my styling in my css
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control'})

        