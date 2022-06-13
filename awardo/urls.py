from django.conf.urls import url, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name= 'home'),
    url(r'^search/', views.search_projects, name='searched'),
    url(r'^project/(\d+)', views.get_project, name='searched_projects'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)