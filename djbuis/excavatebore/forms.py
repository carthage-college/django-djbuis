#Include django.forms
import datetime
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from models import ExcavateModel #Include the model that goes with this form
from django.contrib.admin import widgets #Import this if you want to change the layout of certain fields
import re

class ExcavateForm(forms.ModelForm):

    #This is needed if you want to add error messages, labels or additional validation for fields
    def __init__(self, *args, **kwargs):
        super(ExcavateForm, self).__init__(*args,**kwargs)
        
    #error messages are found below    
    def clean_applicant_name(self):    
        name = self.cleaned_data['applicant_name']
        if not re.match(r'^((?:[a-zA-Z]+\s?){1,2}[a-zA-Z]+)$', name):
            raise forms.ValidationError('Enter a name with no special characters or extra spaces')
        return name
        
    def clean_dates(self):
        date1 = self.cleaned_data['start_date']
        date2 = self.cleaned_data['end_date']
        
        if date1 < datetime.date.today():
            raise forms.ValidationError('The end date cannot be in the past!')
                
        if date2 < datetime.date.today():
            raise forms.ValidationError('The end date cannot be in the past!')
            
        elif date2 < date1:
            raise forms.ValidationError('The end date cannot be before the start date!')
                
        del cleaned_data['start_date', 'end_date']
    
    def clean(self):
        cleaned_data = self.cleaned_data #Grabs the clean data
        
        return cleaned_data 
        #Return the data back to the form
        
    #A function that will print values in a format, when we email the form
    def as_string(self):
        return '''
                Please check Django admin page for this new submission ->
        
                Applicant name: %s\n
                Phone number: %s\n
                Company: %s\n
                Type of work: %s\n
                Bore: %s\n
                Reason: %s\n
                Location: %s\n
                Start date: %s\n
                End date: %s\n
                ''' % (self.cleaned_data['applicant_name'],
                       self.cleaned_data['phone'],
                       self.cleaned_data['company'],
                       self.cleaned_data['excavate_bore'],
                       self.cleaned_data['reason'],
                       self.cleaned_data['location'],
                       self.cleaned_data['start_date'],
                       self.cleaned_data['end_date'])        
        
    #Global settings for the model    
    class Meta:
        model = ExcavateModel #All fields come from the model 'ExcavateModel'
        exclude = ['reviewed_by','meeting_held_with_applicant','date_of_approval','server'] #These fields are not seen in the form (in the html page)

        widgets = {
            'excavate_bore' : forms.RadioSelect(),
            'start_date' : forms.DateInput(attrs={'type': 'date'}),
            'end_date' : forms.DateInput(attrs={'type': 'date'}),
        }
