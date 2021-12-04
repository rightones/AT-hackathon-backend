from django.shortcuts import render

# Create your views here.
from django_filters import filters
from rest_framework import viewsets

from .models import Team
from .serializers import TeamSerializer


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    filterset_fields = ['related_positions__name']
    filter_backends = [filters.SearchFilter]
    search_fields = ['subject']