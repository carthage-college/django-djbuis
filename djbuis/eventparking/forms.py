from django import forms
from django.contrib.admin import widgets
from djbuis.eventparking.models import Parking
from django.db import models

class ParkingForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(ParkingForm, self).__init__(*args, **kwargs)
		
		
	class Meta:
		model = Parking
		exclude = ['parking_arrangements_required','date_completed']
		widgets = {
			'event_date': forms.DateInput(attrs={'type': 'date'}),
			'event_time': forms.TimeInput(attrs={'type': 'time'}),
			'crowd_estimate': forms.TextInput(attrs={'type': 'number'}),
		}
