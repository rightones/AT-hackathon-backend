# Generated by Django 3.2.9 on 2021-12-04 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_portfolio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
