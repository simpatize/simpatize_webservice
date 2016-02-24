from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    place_type = models.CharField(max_length=100)
    geolocation = models.CharField(max_length=100)
    cause = models.CharField(max_length=20)

    def __str__(self):
        return self.name
