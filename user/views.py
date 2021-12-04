from django.shortcuts import render
from user.models import Profile
from rest_framework import viewsets
from user.serializers import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
