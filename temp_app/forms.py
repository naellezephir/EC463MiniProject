from django import forms
from .models import Rooms
from django.forms import ModelForm

class RoomForm(ModelForm):
	class Meta:
		model = Rooms
		fields = ['nickname', 'user_name']

