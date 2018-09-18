from django.db import models

# Create your models here.

# created model for each room object, need to connect with external modules
class Room(models.Model):
	nickname = models.CharField(max_length = 50)
	temperature = models.IntegerField()
	humidity = models.IntegerField()
	user_name = models.CharField(max_length = 256)

