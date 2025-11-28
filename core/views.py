from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm  # We will need to create this form
from django.contrib.auth.decorators import login_required

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'auth/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # Remember Me Logic
            if request.POST.get('remember_me'):
                # Keep session for 2 weeks (1209600 seconds)
                request.session.set_expiry(1209600)
            else:
                # Expire session when browser closes
                request.session.set_expiry(0)
                
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    # Handle GET requests for logout (optional, but good for simple links)
    logout(request) 
    return redirect('home')
