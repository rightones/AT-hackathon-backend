from rest_framework import serializers

from .models import Position, Topic




class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    related_positions = PositionSerializer()
    class Meta:
        model = Topic
        fields="__all__"
