from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    class Category(models.IntegerChoices):
        link = 1
        text = 2

    category = models.IntegerField(choices=Category.choices)
    content = models.TextField()


class PortfolioProfile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    portfolios = models.ManyToManyField(Portfolio, related_name="profiles")
