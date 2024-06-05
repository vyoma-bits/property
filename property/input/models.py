from django.db import models

class Location(models.Model):
    property_id = models.IntegerField()
    location = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    parcel_size = models.CharField(max_length=255)
    price_per_acre = models.CharField(max_length=255)
    micro_market = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)

    # New field for total price calculation
    total_price = models.FloatField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate total price before saving the model
        try:
            parcel_size_value = float(self.parcel_size)  # Assuming parcel_size is a number
            price_per_acre_value = float(self.price_per_acre)  # Assuming price_per_acre is a number
            self.total_price = parcel_size_value * price_per_acre_value
        except ValueError:
            # Handle potential conversion errors gracefully (optional)
            pass

        super().save(*args, **kwargs)


    def __str__(self):
        return self.location
class Broker(models.Model):
    name=models.CharField(max_length=100)
    phone_number=models.CharField(max_length=12)
    email=models.EmailField(max_length = 254)
    percentage_of_commission=models.IntegerField(default=0)
    property_id=models.ForeignKey(Location,on_delete=models.CASCADE)




