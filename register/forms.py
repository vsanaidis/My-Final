from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# I create the form for the signup (register) of the user
class SignupForm(UserCreationForm):
    # I added fields (custom) like the email or the terms_checkbox which will be later updated with the link to the terms.
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    phone_number = forms.CharField(max_length=15, required=True)
    terms_checkbox = forms.BooleanField(required=True)

    class Meta:
        # I associate the model I will use
        model = get_user_model()
        fields = ('email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2')

    def clean_email(self): 
        #I create a custom validation for the email that should end with @acg.edu
        email = self.cleaned_data.get('email')
        if not email.endswith('@acg.edu'):
            raise ValidationError("Email must end with @acg.edu")
        return email
