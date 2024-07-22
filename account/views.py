from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import CustomPasswordChangeForm



def account_view(request):
    #I make a custom user authentication insteat of @login_required
    if request.user.is_authenticated:
        if request.method == 'POST':
            #I create my changepassword form 
            form = CustomPasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                # I save the new user information, in this case the password, in later updates even more.
                user = form.save()
                update_session_auth_hash(request, user)  # Important to keep the user logged in
                messages.success(request, 'Your password was successfully updated!')
                return redirect('account')
            else:
                # Spawn a message to let the user know he didnt fill the forms correctly.
                messages.error(request, 'Please correct the error below.')
        else:
            # I take the request GET from the user
            form = CustomPasswordChangeForm(request.user)
        #redirects the user to the account.html when the user is authenticated
        return render(request, 'account.html', {'form': form})
    else:
        #if user is not authenticated he/she gets redirected to login again.
        return redirect("login")

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
    if request.method == 'POST':
        # I create the form for my user login
        form = LoginForm(request.POST)
        if form.is_valid():
            #if the form is valid then it gets the data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #user authentication
            user = authenticate(request, username=username, password=password)
            if user is not None:
                #if my user is not None which means user exists then it logins the user (request,user)
                login(request, user)
                messages.success(request, f'Welcome, {user.first_name} {user.last_name}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid email or password!')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

#I used the built-in django logout form
def user_logout(request):
    logout(request)#it logouts the user on request
    return redirect('login')#redirects to login (login.html)

@login_required #here I used the built-in login_required form
def change_password(request):
    if request.method == 'POST':
        #I create the user passwordchange form
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important to keep the user logged in
            messages.success(request, 'Your password was successfully updated!')
            return redirect('account')
        else:
            #for field, errors in form, this means that if there are any errors it displays the error
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
                    return redirect('change_password')
    else:
        form = CustomPasswordChangeForm(request.user)
        
    
    return render(request, 'account.html', {'form': form})