from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from registration.forms import SignUpForm
# from crispy_forms.helper import FormHelper

class SignUpForm(SignUpForm):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)