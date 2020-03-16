from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.home, name ='home'),
    path('registration/', views.Registration, name='registration'),
    path('profile/', views.Profile, name='profile'),
    path('new_site/', views.post_project, name='new_site'),
    path('project/<int:project_id>', views.get_project, name='project'),
    path('search/', views.search_results, name='search'),
    

]