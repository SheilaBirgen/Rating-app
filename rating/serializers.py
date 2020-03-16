from rest_framework import serializers
from .models import Projects, Profile


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ('project_image', 'project_title', 'project_description', 'project_link', 'post_date', 'profile', 'author')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'url', 'bio', 'photo', 'contact_info')
