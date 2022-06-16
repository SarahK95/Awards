"""Awaards URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views
from django.contrib.auth import views as auth_views
from awardo.views import main_view, rate_image

# from registration.backends.simple.views import RegistrationView
# from awardo.forms import RegisterForm




urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'', include('awardo.urls')),
    # url(r'^accounts/register/$',RegistrationView.as_view(form_class=RegisterForm),name='registration_register',),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/',auth_views.LogoutView.as_view(),{'next_page':'/'}),
    
    url(r'', main_view, name="main-view"),
    url(r'^rate/', rate_image, name='rate-view'),
    
]
