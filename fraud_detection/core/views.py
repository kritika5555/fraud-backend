from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  #ensuring user is loggedin to access view
from core.models import *
from .models import Transaction
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auth_login(request, user)  # Log the user in after registration
            return redirect('login')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}!")
                return redirect("home")  # Redirect to home page after login
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    
    else:
        form = AuthenticationForm()
    
    return render(request, "login.html", {"form": form})


def home(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-timestamp')[:7]
    return render(request, 'home.html', {'transactions': transactions})






