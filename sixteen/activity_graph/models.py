from django.db import models
from django.contrib.auth.models. import User

class affinity (models.Model):
    user        = models.OneToOneField(User, on_delete = models.CASCADE)

    # Location
    latitude    = models.FloatField()
    longitude   = models.FloatField()

    # Cost
    cost        = 

    # Sports
    water       = models.FloatField()
    novel       = models.FloatField()
    leisure     = models.FloatField()
    coolShit    = models.FloatField()

    # Environments
    forest =
