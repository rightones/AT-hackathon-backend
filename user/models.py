from django.db import models
from django.contrib.auth.models import User
from django_s3_storage.storage import S3Storage

storage = S3Storage(aws_s3_bucket_name="at-hackathon")


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nickname = models.CharField(max_length=20)

    class Gender(models.IntegerChoices):
        남성 = 1
        여성 = 2
        기타 = 3

    gender = models.IntegerField(choices=Gender.choices)

    school = models.CharField(max_length=20, null=True, blank=True)
    major = models.CharField(max_length=40, null=True, blank=True)
    email = models.EmailField()
    address = models.TextField(null=True, blank=True)

    image = models.ImageField(storage=storage, upload_to="profile/image/", null=True, blank=True)
    document = models.FileField(storage=storage, upload_to="profile/document/", null=True, blank=True)

    description = models.TextField()
    group_category1_favorite = models.BooleanField(default=False)
    group_category2_favorite = models.BooleanField(default=False)
    group_category3_favorite = models.BooleanField(default=False)

    portfolio = models.TextField(blank=True)
