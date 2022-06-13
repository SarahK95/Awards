import datetime as dt
from django.shortcuts import render
from .models import *
from .forms import *
from django.conf import settings
from django.templatetags.static import static
from django.shortcuts import render, redirect, render_to_response, HttpResponseRedirect
from django.http import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    projects = Projects.get_projects()
    date = dt.date.today()
    return render(request, 'index.html', {"date": date, "projects":projects})

def signup(request):
    if request.method=='POST':
        form= SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Succesful {username}!')
            return redirect('/')
        
    else:
        form = SignUpForm()
    return render (request, 'registration/registration_form.html', {'form':form})        
    