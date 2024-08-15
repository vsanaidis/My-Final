from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
#a simple render of my index.html
def index_view(request):
    return render(request, 'index.html')

def search_friends(request):

    username = request.user.username
    query = request.GET.get('username')
    user = get_object_or_404(User, username=username)
    if query:
        users = User.objects.filter(username__icontains=query)
    else:
        users = User.objects.none()
    context = {
        'users': users,
        'query': query,
        'profile_user': user,
    }

    return render(request, 'search_results.html', context) 