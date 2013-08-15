from django import forms
from djbuis.maintenance.models import Maintenance
from django.db import models

class MaintenanceForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(MaintenanceForm, self).__init__(*args, **kwargs)
		self.fields['description_of_service'].label = 'Description of requested service:'
		self.fields['name'].label = 'Your name:'
		self.fields['office'].label = 'Office(building and room number):'
		
	class Meta:
		model = Maintenance
		exclude = ['date_recieved', 'date_completed', 'repaired_by', 'delay_due_to', 'delayed_repair_scheduled', 'departmental_charge', 'account_number', 'comments']
		widgets = {
			'description_of_service': forms.Textarea(attrs={'cols':70,}),
			'other_location_information': forms.TextInput(attrs={'size': 60})
		}
