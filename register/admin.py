from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'phone_number','password')
    search_fields = ('email', 'first_name', 'last_name')
admin.site.register(User,UserAdmin)