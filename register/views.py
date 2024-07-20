from django.shortcuts import render, redirect
from .forms import SignupForm

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Update this to the name of your login URL
    else:
        form = SignupForm()
    return render(request, 'register.html', {'form': form})
