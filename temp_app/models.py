from django.db import models

# Create your models here.
class Rooms(models.Model):
	nickname = models.CharField(max_length = 50)
	temperature = models.IntegerField()
	humidity = models.IntegerField()
	username = models.ForiegnKey(user_profile.username, on_delete = models.CASCADE)

