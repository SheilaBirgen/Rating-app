from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('registration/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('',views.home, name ='home'),

]