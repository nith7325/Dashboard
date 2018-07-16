from django.db import models

# Create your models here.
class Album(models.Model):
	date = models.CharField(max_length=250)
	market = models.CharField(max_length=500)
	alert=models.CharField(max_length=100)
	alert_details = models.CharField(max_length=1000)

def __str__ (self):
    return '%s %s %s %s' (self.date, self.market, self.alert, self.alert_details)