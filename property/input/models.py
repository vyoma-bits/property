from django.db import models

class Property(models.Model):
    name = models.CharField(max_length=255)
    # Other property fields...
    google_location = models.CharField(max_length=255, blank=True)  # Optional location string
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # Latitude
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)  # Longitude
