from django.contrib.auth.models import User
from django.db import models
from recommend.models import Position


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    specials = models.TextField()
    leader = models.ForeignKey(
        User, related_name="leader_teams", on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User, related_name="member_teams")

    class Status(models.IntegerChoices):
        NORMAL = 0
        CLOSED = 1

    status = models.IntegerField(default=0, choices=Status.choices)
    category = models.IntegerField()


class TeamPosition(models.Model):
    required_positions = models.ManyToManyField(Position)
    user = models.ForeignKey(
        User, related_name="team_positions", on_delete=models.SET_NULL, null=True
    )
    team = models.ForeignKey(
        Team, related_name="positions", on_delete=models.SET_NULL, null=True
    )
