from django.db import models

# Create your models here.
class bmp_data(models.Model):
    #time = models.DateTimeField('date published')
    temperature = models.FloatField()
    pressure = models.FloatField()
    altitude = models.FloatField()
    