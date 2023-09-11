from django.db import models

# Create your models here.
class CO2(models.Model):
    date = models.DateTimeField()
    average = models.FloatField()

    class Meta:
        ordering = ('date',)

class NO2(models.Model):
    date = models.DateTimeField()
    average = models.FloatField()

    class Meta:
        ordering = ('date',)

class PM25(models.Model):
    date = models.DateTimeField()
    average = models.FloatField()

    class Meta:
        ordering = ('date',)

class PM10(models.Model):
    date = models.DateTimeField()
    average = models.FloatField()

    class Meta:
        ordering = ('date',)

class Location(models.Model):

    sensor_ID = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self):
        return self.sensor_ID
