from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from PIL import Image
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=200,blank=True)
    photo = models.ImageField(upload_to = 'profiles/', blank=True, default='profiles/default.jpg')
    contact_info = models.CharField(max_length = 20, blank=True)
   
    def delete_profile(self):
        self.delete()
    
    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    @classmethod
    def get_profiles(cls):
        profile = cls.objects.all()
        return profile

# Create Profile when creating a User
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

# Save Profile when saving a User
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save


class Project(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)
    link = models.CharField(max_length=150)
    post_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default='1')
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')


    def __str__(self):
        return f'{self.profile.user.username}'

    @classmethod
    def get_project_by_id(cls, id):
        try:
            proj = Project.objects.get(pk=id)
        except ObjectDoesNotExist:
            raise Http404()
        return proj

    @classmethod
    def get_project(cls):
        project = cls.objects.all()
        return project

    @classmethod
    def search_by_title(cls, search_term):
        project = cls.objects.filter(title__icontains=search_term)
        return project

class Rating(models.Model):
    design = models.PositiveSmallIntegerField(default=0)
    usability = models.PositiveSmallIntegerField(default=0)
    content = models.PositiveSmallIntegerField(default=0)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='1')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default='project_folder/')

    def __str__(self):
        return f'{self.design}'
