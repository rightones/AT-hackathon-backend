from django.shortcuts import render

# Create your views here.
from rest_framework import filters
from rest_framework import viewsets

from .models import Team, TeamPosition
from .serializers import TeamSerializer, TeamPositionSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_fields = ['related_positions__name', "category"]
    filter_backends = [filters.SearchFilter]
    search_fields = ['subject']


class TeamPositionViewSet(viewsets.ModelViewSet):
    queryset = TeamPosition.objects.all()
    serializer_class = TeamPositionSerializer
    filterset_fields = ['team__id']