from rest_framework import serializers

from recommend.serializers import PositionSerializer
from .models import Team, TeamPosition


class TeamPositionSerializer(serializers.ModelSerializer):
    required_positions = PositionSerializer()
    class Meta:
        model = TeamPosition
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    positions = TeamPositionSerializer(many=True)
    class Meta:
        model = Team
        fields = "__all__"