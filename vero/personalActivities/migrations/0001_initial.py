# Generated by Django 3.2.7 on 2021-10-26 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('description', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('description', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalActivites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, unique=True)),
                ('description', models.CharField(max_length=254)),
                ('image_URL', models.URLField(blank=True, max_length=1000)),
                ('video_URL', models.URLField(blank=True, max_length=1000)),
                ('lecture', models.CharField(blank=True, max_length=1000000)),
                ('pub_data', models.DateTimeField(verbose_name='date published')),
                ('duration', models.DurationField()),
                ('activityType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='personalActivities.activitytype')),
                ('categories', models.ManyToManyField(to='personalActivities.ActivityCategory')),
            ],
        ),
    ]
