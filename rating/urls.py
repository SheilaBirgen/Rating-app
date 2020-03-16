from django.urls import path, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('profiles', views.ProfileView)

urlpatterns = [
    path('',views.home, name ='home'),
    path('registration/', views.Registration, name='registration'),
    path('profile/', views.Profile, name='profile'),
    path('new_site/', views.post_project, name='new_site'),
    path('project/<int:project_id>', views.get_project, name='project'),
    path('search/', views.search_results, name='search'),
    path('api/projects/', views.ProjectView.as_view()),
    path('api_token_auth/', obtain_auth_token),
    path('profile_api/', include(router.urls)),
]