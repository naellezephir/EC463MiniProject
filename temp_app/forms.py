from django import forms
from .models import Rooms

class RoomForm(ModelForm):
	class Meta:
		model = Rooms
		fields = ['nickname', 'user_name']

