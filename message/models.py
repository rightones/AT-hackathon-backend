from django.db import models
from django.contrib.auth.models import User

from team.models import TeamPosition


class Message(models.Model):
    team_position = models.ForeignKey(TeamPosition, on_delete=models.CASCADE)
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_sent')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_received')

