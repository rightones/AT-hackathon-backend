from django.contrib.auth.models import User
from django.db import models
from django_s3_storage.storage import S3Storage
from recommend.models import Position


storage = S3Storage(aws_s3_bucket_name="at-hackathon")


class Team(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    specials = models.TextField()
    leader = models.ForeignKey(
        User, related_name="leader_teams", on_delete=models.CASCADE
    )
    members = models.ManyToManyField(User, related_name="member_teams", blank=True, null=True)

    class Status(models.IntegerChoices):
        NORMAL = 0
        CLOSED = 1

    status = models.IntegerField(default=0, choices=Status.choices)
    category = models.IntegerField()
    subject = models.TextField()
    image = models.ImageField(storage=storage, upload_to="profile/image/", null=True)



class TeamPosition(models.Model):
    required_positions = models.ForeignKey(Position, related_name="team_positions", on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(
        User, related_name="team_positions", on_delete=models.SET_NULL, null=True, blank=True
    )
    team = models.ForeignKey(
        Team, related_name="positions", on_delete=models.SET_NULL, null=True
    )
