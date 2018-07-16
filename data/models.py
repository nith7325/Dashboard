from django.db import models

# Create your models here.
class Album(models.Model):
	date = models.CharField(max_length=250)
	market = models.CharField(max_length=500)
	alert=models.CharField(max_length=100)
	alert_details = models.CharField(max_length=1000)

	def __str__(self):
		return self.market + ' _ ' + self.date
		
# class Song(models.Model):
# 	album = models.ForeignKey(Album, on_delete=models.CASCADE)
# 	file_type = models.CharField(max_length=10)
# 	song_title = models.CharField(max_length=250)

# 	def __str__(self):
# 		return self.song_title


