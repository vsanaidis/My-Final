from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm,UserUpdateForm,ProfileUpdateForm
from django.http import HttpResponseBadRequest
from .models import Profile
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User 


@login_required
def account_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    u_form = UserUpdateForm(instance=request.user)
    p_form = ProfileUpdateForm(instance=profile)
    password_form = PasswordChangeForm(user=request.user)

    if request.method == 'POST':
        if 'update_profile' in request.POST:
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, 'Your profile has been updated!')
                return redirect('account')
        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(request.user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
                return redirect('account')
        elif 'update_picture' in request.POST:  # Check if the picture update is being made
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)
            if p_form.is_valid():
                p_form.save()
                messages.success(request, 'Your profile picture has been updated!')
                return redirect('account')

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'password_form': password_form
    }
    return render(request, 'account.html', context)
def user_signup(request): #my view for my user registration (custom one created in forms.py)
    if request.method == 'POST':
        # I create the form with the POST request
        form = SignupForm(request.POST)
        if form.is_valid():
            #if my form is valid then it is saved and the user redirected to login after signing up
            form.save()
            return redirect('login')
    else:
        #if method is not posted (valid) the user is redirected back to the register forms register.html
        form = SignupForm()
    return render(request, 'register.html', {'form': form})
def user_login(request):
    # Prevent redirect loop
    if request.user.is_authenticated and 'next' not in request.GET:
        return redirect('account')  # or wherever you want authenticated users to go
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                return redirect('account')  # or your desired redirect after login
            else:
                messages.error(request, 'Invalid username or password!')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

#I used the built-in django logout form
def user_logout(request):
    logout(request)#it logouts the user on request
    return redirect('login')#redirects to login (login.html)

@login_required
def custom_password_change(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password_change_done')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = CustomPasswordChangeForm(user=request.user)
    return render(request, 'change_password.html', {'form': form})

def password_change_done(request):
    return render(request, 'password_change_done.html')

@login_required
def profile_picture_update(request):
    profile, created = Profile.objects.get_or_create(user=request.user)  # Ensure you get the profile instance

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=profile)  # Correctly instantiate with the profile
        if form.is_valid():
            form.save()  # Save the profile with the new photo
            messages.success(request, 'Your picture has been changed!')
            return redirect('account')
    else:
        form = ProfileUpdateForm(instance=profile)  # Show the current profile picture in the form

    return render(request, 'account.html', {'form': form})  # Pass the form to the template if needed

def user_profile(request, username):
    user = get_object_or_404(User, username=username)
    return render(request, 'user_profile.html', {'profile_user': user})