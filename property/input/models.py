from django.db import models

class Location(models.Model):
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    parcel_size = models.CharField(max_length=255)
    price_per_acre = models.CharField(max_length=255)
    micro_market = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    def __str__(self):
        return self.location
