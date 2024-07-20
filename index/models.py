from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import messages

def user_search(request):
    query = request.GET.get('q')
    users = User.objects.all()  
    
    if query:
        users = users.filter(username__icontains=query)  
    
    context = {
        'users': users,
        'query': query,
    }
    
    return render(request, 'user_search.html', context)