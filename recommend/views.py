from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from recommend.models import Topic
from recommend.serializers import TopicSerializer


class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filterset_fields = ['related_positions__name']