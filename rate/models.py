from django.db import models
from django.contrib.auth.models import User


class Rate(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rates",
    )
    rate_from = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="rated",
    )

    rate1 = models.IntegerField()
    rate2 = models.IntegerField()
