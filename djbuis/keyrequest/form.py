#Include django.forms
from django import forms
from djbuis.keyrequest.models import Keys #Don't forget to import your models!
from django.core.exceptions import ValidationError #This is so we can make error messages
from django.core import validators #This is so we can use regex

# Create your forms here.
class ModelForm(forms.ModelForm):	
    #This is needed if you want to add error messages, labels or additional validation for fields
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		
		self.fields['contact_number'].validators = [validators.RegexValidator(regex='^1?-?\(?\d{3}\)?-?\d{3}-?\d{4}$', message='enter a valid phone number', code='bad_phone')]
		self.fields['account'].label = "Account to Charge"
		self.fields['building'].error_messages['required'] = 'You did not fill in the first field of the "building" column.'
		self.fields['room_number'].error_messages = {'required': 'You did not fill in the first field of the "room number" column.', 'invalid': 'You must put a whole number in the "room number" field'}
		self.fields['key_code_if_known'].error_messages['required'] = 'You did not fill in the first field of the "key code if known" column.'
		self.fields['issued_to'].error_messages['required'] = 'You did not fill in the first field of the "issued to" column.'
		
    #Another way to include custom validation
	def clean(self):                                                                                                                                      
		cleaned_data = super(ModelForm, self).clean() #Grabs the clean data

		reason = cleaned_data.get("reason")
		other = cleaned_data.get("other")
		
		if reason == "OTH" and other == "":
			msg = u"Please give a reason for picking \"other\"" #Adds the error message to the field
			self._errors["other"] = self.error_class([msg])

			del cleaned_data["reason"] #Django told me to do this?
			del cleaned_data["other"]
		
		return cleaned_data #Return the data back to the form
    #Global settings for the model	
	class Meta:
		model = Keys #All fields come from the model 'Keys'
		widgets = {
			'reason': forms.RadioSelect() #Turns the select drop down into a radio button select
			}
		exclude = ('dean_sig', 'date_completed',) #These fields are not seen in the form (in the html page)
