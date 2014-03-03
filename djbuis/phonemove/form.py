from django import forms
from models import Phone
from django.core.exceptions import ValidationError
from django.core import validators

# Create your forms here.
class ModelForm(forms.ModelForm):	
	def __init__(self, *args, **kwargs):
		super(ModelForm, self).__init__(*args, **kwargs)
		self.fields['name'].label = "Name of User"
		self.fields['department'].label = "Department"
		self.fields['user_number'].label = "User\'s Phone Number or Extension"
		self.fields['request'].label = "What are you requesting?"
		self.fields['from_location'].label = "From Location"
		self.fields['to_location'].label = "To Location"
		self.fields['caller_id'].label = "Caller ID Name Change or Add"
		self.fields['date_of_change'].label = "Date of move, add, change"
		self.fields['email'].label = "Check this box if you would like the form to be emailed to you upon completion."
		self.fields['user_number'].validators = [validators.RegexValidator(regex='^1?-?\(?\d{3}\)?-?\d{3}-?\d{4}$|NEW', message='You entered invalid text. You can either enter a phone number or the word \"NEW\"', code='bad_phone')]
		self.fields['name'].error_messages = {'required': 'Please fill in a name.'}
		self.fields['department'].error_messages = {'required': 'Please fill in a department.'}
		self.fields['user_number'].error_messages = {'required': 'Please fill in a user number.'}
		self.fields['request'].error_messages = {'required': 'Please select one of the answers below.'}
		self.fields['from_location'].error_messages = {'required': 'Please fill in a from location.'}
		self.fields['to_location'].error_messages = {'required': 'Please fill in a to location.'}
		self.fields['caller_id'].error_messages = {'required': 'Please fill in a caller id.'}
		self.fields['date_of_change'].error_messages = {'required': 'Please fill in a date of change.'}
	def to_mail(self):
		if self.cleaned_data['email'] == True:
			return "%s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n "% [self.cleaned_data['name'], self.cleaned_data['department'], self.cleaned_data['user_number'], self.cleaned_data['request'], self.cleaned_data['from_location'], self.cleaned_data['to_location'], self.cleaned_data['caller_id'], self.cleaned_data['date_of_change']]
	class Meta:
		model = Phone
		widgets = {
			'from_location': forms.Textarea(),
			'to_location': forms.Textarea(),
			'caller_id': forms.Textarea(),
			'email': forms.CheckboxInput(),
			'request': forms.RadioSelect(),
			'date_of_change': forms.DateInput(attrs={'type':'date'})
			}
