from django.db import models
from django.contrib.auth.models. import User

class ratings (models.Model):
    # Location
    latitude    = models.FloatField()
    longitude   = models.FloatField()

    # Cost
    cost        = models.FloatField()

    # Sports
    aqua        = models.FloatField()
    novel       = models.FloatField()
    leisure     = models.FloatField()
    coolShit    = models.FloatField()

    # Environments
    forest      = models.FloatField()
    mount       = models.FloatField()
    water       = models.FloatField()

    class Meta:
        abstract = True

class extendedUser(models.Model):
    user        = models.OneToOneField(User, on_delete = models.CASCADE)

class business (models.Model):
    yelp_rate   = models.FloatField()
    address     = models.CharField()
