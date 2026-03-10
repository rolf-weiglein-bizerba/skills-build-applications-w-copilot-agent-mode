from djongo import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='octofit_tracker_user_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='octofit_tracker_user_permissions',
        blank=True
    )
    class Meta:
        app_label = 'octofit_tracker'

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'
