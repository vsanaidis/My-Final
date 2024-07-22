from django.contrib import admin
from .models import Notes
# Register your models here.
#registering my notes model here to be able to see it in the admin view.
admin.site.register(Notes)
