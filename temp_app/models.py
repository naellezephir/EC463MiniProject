from django.db import models

# Create your models here.
class Rooms(models.Model):
	nickname = models.CharField(max_length = 50)
	temperature = models.IntegerField()
	humidity = models.IntegerField()
	user_name = models.CharField(max_length = 256)

