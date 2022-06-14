import datetime as dt
from email import message
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

def register(request):
    if request.method=='POST':
        form=  RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Succesful {username}!')
            return redirect('/')
        
    else:
        form =  RegisterForm()
    return render (request, 'registration/registration_form.html', {'form':form})       


@login_required(login_url='/accounts/login/')
def search_projects(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Projects.search_projects(search_term)
        message = f'{search_term}'
        return render (request, 'search.html', {'message':message, 'projects':searched_projects})
    
    else :
        message = "You haven't searched anything"
        return render(request, 'search.html',{'message':message})
    
    
def get_project(request, id):    
    
    try:
        project = Projects.objects.get(pk=id)
    except ObjectDoesNotExist:
        raise Http404()
    
    return render(request, 'project.html', {'project':project}) 

@login_required(login_url='/accounts/login/')
def new_project(request):
    current_user = request.user
    if request.method =='POST':
        form = NewProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.Author = current_user
            project.save()
        return redirect ('home')
    else:
        form = NewProjectForm()
    return render(request, 'new_project.html', {'form':form})        
        
        
@login_required(login_url='/accounts/login/') 
def profile(request):
    current_user = request.user
    Author = current_user
    projects = Projects.get_by_author(Author)
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            profile = form.save(commit= False)
            profile.save()
        return redirect('profile')
    else:
        form = ProfileUpdateForm()
        return render(request, 'registration/profile.html', {'form':form, 'projects':projects})    
           