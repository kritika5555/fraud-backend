from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import User  # Import your custom User model if using it

class CustomUserCreationForm(UserCreationForm):
    fullname = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User  # Use your custom User model if applicable
        fields = [ 'fullname', 'phone', 'password1', 'password2']