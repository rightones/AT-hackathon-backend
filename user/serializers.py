from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        return Profile(user=user, **validated_data)