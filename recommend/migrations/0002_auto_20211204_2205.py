# Generated by Django 3.2.9 on 2021-12-04 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
