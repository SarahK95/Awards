from tkinter import CASCADE
from django.db import models
import datetime as dt
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    prof_pic = models.ImageField(upload_to = 'prof_pics/', blank=True)
    