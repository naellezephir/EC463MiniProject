from django import forms
from .models import Rooms
from django.forms import ModelForm

class RoomForm(forms.ModelForm):
	class Meta:
		model = Rooms
		fields = ['nickname','temperature', 'humidity']

