from django import forms
from .models import Room
from django.forms import ModelForm

# created form to add a room if one isn't connected
class RoomForm(forms.ModelForm):
	class Meta:
		model = Room
		fields = ['nickname','temperature', 'humidity']

