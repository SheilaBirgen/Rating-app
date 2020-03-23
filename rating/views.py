from django.shortcuts import render, redirect,HttpResponse, Http404, loader
from django.contrib.auth import login as auth_login
from .forms import *
from .models import *
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.contrib.auth import login, logout

# Create your views here.
class ProjectView(APIView):
    def get(self, request, format=None):
        project = Project.objects.all()
        serializer = ProjectSerializer(project, many=True)
        return Response(serializer.data)


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    

def home(request):
    today = dt.date.today()
    project = Project.get_project()
    context = {
        "today":today,
        "project":project,
    }
    return render(request, 'index.html', context)

@login_required(login_url='/login/')
def Profile(request):
    photo = Project.get_project()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'You have successfully updated your profile!')
            return redirect('/profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    return render(request, 'profile.html', {"user_form": user_form, "profile_form": profile_form, "photo": photo})

@login_required(login_url='/login/')
def create_profile(request):
    '''View function for user to create their profile'''
    if request.method=="POST":
        form = ProfileUpdateForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('index')
    else:
        form = ProfileUpdateForm()
    return render(request, 'profile.html',{"form":form})
    
def signup(request):
    '''View Function for user signup'''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']

            user = form.save()
            user.save()
            # send_welcome_email(name,email)
            login(request, user)
            return redirect('create_profile')
    else:
        form = SignUpForm()
    template = loader.get_template('registration/signup.html')
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))

def logout_user(request):
    logout(request)

    return redirect(home)


@login_required(login_url='/login')
def post_project(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostProjectForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.author = current_user
            image.save()
        return redirect('/')
    else:
        form = PostProjectForm(auto_id=False)
    return render(request, 'new_project.html', {"form": form})

@login_required(login_url='/login/')
def get_project(request,project_id):
    project =Project.objects.get(pk=project_id)
    return render(request, 'project.html',  {"project":project})

def search_results(request):
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get('project')
        searched_project = Project.search_by_title(search_term)
        message = f'{search_term}'

        context = {
            "message": message,
            "project": searched_project
        }
        return render(request, 'search.html', context)
    else:
        message = "Search a project by title"
        return render(request, 'search.html', {"message": message})