from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    photo = models.ImageField(upload_to = 'profiles/', blank=True, default='profiles/default.jpg')

    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

class Project(models.Model):
    project_title = models.CharField(max_length=30)
    project_description = models.TextField(max_length=255)
    pub_date = models.DateTimeField(auto_now=True)
    project_author = models.ForeignKey(User, on_delete=models.CASCADE)

