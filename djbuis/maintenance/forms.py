#Include django.forms
from django import forms
from django.core import validators #I need this for validation

from djbuis.maintenance.models import Maintenance #Need this for Meta options!

#Class that consists of all the fields in the form
class MaintenanceForm(forms.ModelForm):
    
    #Need this to change labels, validations and error messages
    def __init__(self, *args, **kwargs):
        super(MaintenanceForm, self).__init__(*args, **kwargs)
        
        #Changing a couple of labels here
        self.fields['description_of_service'].label = 'Description of requested service:'
        self.fields['name'].label = 'Your name:'
        self.fields['office'].label = 'Office (building and room number):'
        
        #Validating fields here
        self.fields['building'].validators = [validators.RegexValidator(regex='^.+$', message='Invalid building', code='bad building')]
        self.fields['floor'].validators = [validators.RegexValidator(regex='^[a-zA-Z0-9]+$', message='Invalid floor', code='a')]
        self.fields['room'].validators = [validators.RegexValidator(regex='^[0-9]+$', message='Invalid room', code='bad room')]
        self.fields['other_location_information'].validators = [validators.RegexValidator(regex='^.+$', message='Invalid characters', code='bad characters')]
        self.fields['description_of_service'].validators = [validators.RegexValidator(regex='^.+$', message='Invalid characters', code='bad characters')]
        self.fields['name'].validators = [validators.RegexValidator(regex='^.+$', message='Invalid name', code='bad name')]
        self.fields['office'].validators = [validators.RegexValidator(regex='^.+$', message='Invalid office', code='bad office')]
        
        #NEED TO ADD THIS IN?
        #self.fields['campus_telephone'].validators = [validators.RegexValidator(regex='', message='', code='a')]
        
        #Custom error messages
        self.fields['building'].error_messages = {'required': 'Please enter a building name', 'invalid': 'Invalid building name'}
        self.fields['floor'].error_messages = {'required': 'Please enter a floor', 'invalid': 'Invalid floor'}
        self.fields['room'].error_messages = {'required': 'Please enter a room', 'invalid': 'Invalid room number'}
        self.fields['other_location_information'].error_messages = {'required': 'Please enter other location information', 'invalid':'Invalid characters in location information'}
        self.fields['description_of_service'].error_messages = {'required':'Please enter a description', 'invalid':'Invalid characters in description'}
        self.fields['name'].error_messages = {'required': 'Please enter a name', 'invalid':'Invalid name'}
        self.fields['campus_telephone'].error_messages = {'required': 'Please enter your campus phone number','invalid':'Invalid phone number'}
        self.fields['office'].error_messages = {'required': 'Please enter an office', 'invalid':'Invalid office'}
    
    #Global options    
    class Meta:
        model = Maintenance #What class we use to define our fields
        exclude = ['date_recieved', 'date_completed', 'repaired_by', 'delay_due_to', 'delayed_repair_scheduled', 'departmental_charge', 'account_number', 'comments'] #We're not going to see these fields in the form
        widgets = { #Changing how fields are seen
            'description_of_service': forms.Textarea(attrs={'cols':70,}), #Viewed as a textarea
            'other_location_information': forms.TextInput(attrs={'size': 60})
        }
