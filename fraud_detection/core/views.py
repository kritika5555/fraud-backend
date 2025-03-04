from django.shortcuts import render
from core.models import *

def home(request):

    return render (request, "home.html")

def login(request):
    return render (request, "login.html")








