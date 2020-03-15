from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pic', 'bio', 'contact_info']


class PostProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['image', 'title', 'description', 'link']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['design', 'usability', 'content']