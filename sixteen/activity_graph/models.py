from django.db import models
from django.contrib.auth.models import User

class ratings (models.Model):
    # Location
    latitude    = models.FloatField(default = 38.6270)
    longitude   = models.FloatField(default = 90.1994)

    # Cost
    cost        = models.FloatField(default = 0.01)

    # Sports
    aqua        = models.FloatField(default = 0.01)
    novel       = models.FloatField(default = 0.01)
    leisure     = models.FloatField(default = 0.01)
    coolShit    = models.FloatField(default = 0.01)

    # Environments
    forest      = models.FloatField(default = 0.01)
    mount       = models.FloatField(default = 0.01)
    water       = models.FloatField(default = 0.01)

    class Meta:
        abstract = True

class extendedUser(ratings):
    user        = models.OneToOneField(User, on_delete = models.CASCADE)
    rate_counts = models.IntegerField(default = 0)

    def __str__(self):
        return "%s's profile" % self.user

class business (ratings):
    name        = models.CharField(max_length = 250, default = 'Business Name')
    yelp_rate   = models.FloatField(default = 2)
    address     = models.CharField(max_length = 250)
    def __str__(self):
        return '%s \n c%s' % (self.name, self.address)
