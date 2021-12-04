# Generated by Django 3.2.9 on 2021-12-04 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('color', models.CharField(blank=True, max_length=7, null=True)),
                ('related_positions', models.ManyToManyField(related_name='topics', to='recommend.Position')),
            ],
        ),
        migrations.CreateModel(
            name='OngoingTopicProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('topics', models.ManyToManyField(related_name='ongoing_profiles', to='recommend.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='InterestTopicProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('topics', models.ManyToManyField(related_name='interest_profiles', to='recommend.Topic')),
            ],
        ),
        migrations.CreateModel(
            name='AdeptTopicProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('topics', models.ManyToManyField(related_name='adept_profiles', to='recommend.Topic')),
            ],
        ),
    ]
