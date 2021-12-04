from rest_framework import serializers

from .models import Position, Topic, InterestTopicProfile, AdeptTopicProfile


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class TopicSerializer(serializers.ModelSerializer):
    related_positions = PositionSerializer()
    class Meta:
        model = Topic
        fields="__all__"


class InterestTopicSerializer(serializers.ModelSerializer):
    topics = PositionSerializer(many=True)
    class Meta:
        model = Topic
        fields="__all__"


class AdeptTopicSerializer(serializers.ModelSerializer):
    topics = PositionSerializer(many=True)
    class Meta:
        model = Topic
        fields="__all__"


class InterestTopicUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = InterestTopicProfile
        fields="__all__"


class AdeptTopicUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdeptTopicProfile
        fields="__all__"