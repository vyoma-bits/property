from django.db import models
from input.models import Location
class enquiry(models.Model):
    property_id=models.ForeignKey(Location,on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    city=models.CharField(max_length=20)
    phone_number=models.CharField(max_length=11)
    info=models.CharField(max_length=250)
# Create your models here.
