from django.db import models
from django.contrib.auth.models. import User

class affinity (models.Model):
    user        = models.OneToOneField(User, on_delete = models.CASCADE)

    # Location
    latitude    = models.FloatField()
    longitude   = models.FloatField()

    # Cost
    cost        = models.FloatField()

    # Sports
    aquatic     = models.FloatField()
    novel       = models.FloatField()
    leisure     = models.FloatField()
    coolShit    = models.FloatField()

    # Environments
    forest      = models.FloatField()
    mount       = models.FloatField()
    water       = models.FloatField()

class business (models.Model):
    cost        = models.FloatField()
    
