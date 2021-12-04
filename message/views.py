from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action

from message.models import Message
from message.serializers import MessageSerializer



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filterset_fields = ['user_from', "user_to"]

    @action(methods=["POST"])
    def accept(self, request, pk=None):
        message = self.get_object()
        instance = message.team_position
        instance.user = message.user_from
        instance.save()

