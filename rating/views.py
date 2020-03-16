from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from .forms import *
from .models import *
import datetime as dt
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class ProjectView(APIView):
    def get(self, request, format=None):
        projects = Projects.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    

def home(request):
    today = dt.date.today()
    projects = Project.get_projects()
    context = {
        "today":today,
        "projects":projects,
    }
    return render(request, 'index.html', context)

@login_required(login_url='/login')
def Profile(request):
    pics = Projects.get_projects()
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if user_form.is_valid() and p_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'You have successfully updated your profile!')
            return redirect('/profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
    'user_form':user_form,
    'profile_form':profile_form,
    'posts':posts,
    }
    return render(request, 'profile.html', context)

    
def Registration(request):
    '''
    View function for user signup
    '''
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            email = form.cleaned_data['email']
            user = form.save()
            auth_login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


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
    form = ReviewForm()
    try:
        project =Projects.object.all(id=project_id)
        print(project)
    except DoesNotExist:
        raise Http404()
    context ={
        "project": project,
        "form": form
    }
    return render(request, 'project.html', context)

def search_results(request):
    if 'projects' in request.GET and request.GET["projects"]:
        search_term = request.GET.get('projects')
        searched_projects = Projects.search_by_title(search_term)
        message = f'{search_term}'

        context = {
            "message": message,
            "projects": searched_projects
        }
        return render(request, 'search.html', context)
    else:
        message = "Search a project by title"
        return render(request, 'search.html', {"message": message})