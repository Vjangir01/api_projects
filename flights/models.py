from django.db import models

# Create your models here.
class flight_details(models.Model):
    fname = models.CharField(max_length=30)
    fdate = models.DateField()
    ffare = models.FloatField()
    fstart = models.CharField(max_length=30)
    fend = models.CharField(max_length=30)

