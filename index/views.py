from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages
#a simple render of my index.html
def index_view(request):
    return render(request, 'index.html')

