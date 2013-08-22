#Include django.forms
from django import forms
from django.db import models
from django.core import validators
from django.contrib.admin import widgets

#Make sure to include the model
from djbuis.eventparking.models import Parking

#Our form class that contains all fields we will find in the form
class ParkingForm(forms.ModelForm):
	
	#This is needed if you want to add error messages, labels or additional validation for fields
	def __init__(self, *args, **kwargs):
		super(ParkingForm, self).__init__(*args, **kwargs)
		
		#Validation for fields
		self.fields['phone_number'].validators = [validators.RegexValidator(regex='^1?-?\(?\d{3}\)?-?\d{3}-?\d{4}$', message='Enter a valid phone number', code='a')]
		self.fields['event_name'].validators = [validators.RegexValidator(regex='^.+$', message='Invalid event name', code='bad_name')]
		self.fields['event_location'].validators = [validators.RegexValidator(regex='^.+$', message='Invalid event location', code='bad_location')]
		self.fields['contact_person'].validators = [validators.RegexValidator(regex='^.+$', message='Invalid contact person', code='bad_person')]
		
	#Global options for the form class	
	class Meta:
		model = Parking #Use all of the fields from Parking 
		exclude = ['parking_arrangements_required','date_completed'] #Exclude these fields from the form
		widgets = { #Changing the display of certain elements
			'event_date': forms.DateInput(attrs={'type': 'date'}), #Date picker
			'event_time': forms.TimeInput(attrs={'type': 'time'}),
			'crowd_estimate': forms.TextInput(attrs={'type': 'number'}), #This is a number picker
			'phone_number': forms.TextInput(attrs={'maxlength': 16}),
		}
