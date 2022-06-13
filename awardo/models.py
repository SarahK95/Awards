from email.mime import image
from tkinter import CASCADE
from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    prof_pic = models.ImageField(upload_to = 'prof_pics/', blank=True)
    
    def save_profile(self):
        self.save()
        
    def delete_profile(self):
        self.delete()
        
    def __str__(self):
        return self.bio        
    
    
class Projects(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(upload_to = 'images/', blank=True)
    descriptin = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    link = models.URLField()
    Owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    owner_profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, default='1')
    
    def save_project(self):
        self.save()
        
    def delete_project(self):
        self.delete()
        
    @classmethod
    def get_projects(cls):
        projects =cls.objects.all()
        return projects
    
    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects    
    
    @classmethod
    def get_by_owner(cls, Owner):
        projects = cls.objects.filter(Owner=Owner)
        return projects
        
            
        