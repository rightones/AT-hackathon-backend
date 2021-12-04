from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from recommend.models import Topic, Position, InterestTopicProfile, OngoingTopicProfile, AdeptTopicProfile
from recommend.serializers import TopicSerializer, PositionSerializer, AdeptTopicSerializer, InterestTopicSerializer, \
    InterestTopicUpdateSerializer, AdeptTopicUpdateSerializer


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

class TopicViewSet(viewsets.ModelViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    filterset_fields = ['related_positions__id']


class InterestTopicProfileViewSet(viewsets.ModelViewSet):
    queryset = InterestTopicProfile.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return InterestTopicUpdateSerializer
        else:
            return InterestTopicSerializer


class AdeptTopicProfileViewSet(viewsets.ModelViewSet):
    queryset = AdeptTopicProfile.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return AdeptTopicUpdateSerializer
        else:
            return AdeptTopicSerializer
