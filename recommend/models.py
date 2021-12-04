from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=7, null=True, blank=True)
    related_positions = models.ManyToManyField(Position, related_name="topics")


class AdeptTopicProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    topics = models.ManyToManyField(Topic, related_name="adept_profiles")


class InterestTopicProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    topics = models.ManyToManyField(Topic, related_name="interest_profiles")


class OngoingTopicProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    topics = models.ManyToManyField(Topic, related_name="ongoing_profiles")
