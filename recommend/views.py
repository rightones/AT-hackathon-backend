from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from recommend.models import Topic, Position
from recommend.serializers import TopicSerializer, PositionSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filterset_fields = ['related_positions__name']

