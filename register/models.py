from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# I create a model for the user which is based on django's abstractbaseuser built-in
class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)# I indicate if the user is active or not
    is_staff = models.BooleanField(default=False) #I create this to check if the user is staff (has more priviledges or is in a group ) I will initialize this on later updates

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def __str__(self):
        return self.email
    