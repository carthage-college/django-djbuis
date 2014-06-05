#Include django.forms
import datetime
from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from djbuis.excavatebore.models import ExcavateModel #Include the model that goes with this form
from django.contrib.admin import widgets #Import this if you want to change the layout of certain fields
import re

class ExcavateForm(forms.ModelForm):

    #This is needed if you want to add error messages, labels or additional validation for fields
    def __init__(self, *args, **kwargs):
        super(ExcavateForm, self).__init__(*args,**kwargs)
        
    #error messages are found below    
    def clean_name(self):    
        name = self.cleaned_data['applicant_name']
        if not re.match(r'([a-zA-Z]+\s?){1,3}', name):
            raise forms.ValidationError('Enter a name with no special characters or extra spaces')
        return data
        
    def clean_company(self):
        comp = self.cleaned_data['company']
        if not re.match("\w+", comp):
            raise forms.ValidationError('Please do not enter any special characters in your company name.')
        return data
    
    def clean_reason(self):    
        reason = self.cleaned_data['reason_for_excavation_or_boring']
        if not re.match ("\w+", reason):
            raise forms.ValidationError('Please do not enter any special characters in your reason.')
        return data
    def clean_location(self):
        location = self.cleaned_data['location_of_excavation_or_boring']
        if not("\w+", location):
            raise forms.ValidationError('Please do not enter any special characters in your location.')
        return data
    
    def clean(self):
        cleaned_data = self.cleaned_data #Grabs the clean data        
        excavate = cleaned_data.get("excavate")
        bore = cleaned_data.get("bore")
        
        if not excavate and not bore:
            self._errors['excavate'] = self.error_class(['Please select either excavate or bore'])
            del cleaned_data["excavate"] #Django told me to do this?
            del cleaned_data["bore"]
            
        date1 = cleaned_data.get('start_date_for_excavation')
        date2 = cleaned_data.get('projected_end_date_for_excavation')
        
        
        if not date1:
            msg = u"Invalid or past date"
            self._errors['start_date_for_excavation'] = self.error_class([msg])
        else:  
            if date1 < datetime.date.today():
                msg2 = u"The date cannot be in the past!"
                self._errors["start_date_for_excavation"] = self.error_class([msg2]) #Adds the error message to the field
                del cleaned_data["start_date_for_excavation"]
                
        if not date2:
            msg = u"Invalid or past date"
            self._errors['projected_end_date_for_excavation'] = self.error_class([msg])
        else:  
            if date2 < datetime.date.today():
                msg2 = u"The date cannot be in the past!"
                self._errors["start_date_for_excavation"] = self.error_class([msg2]) #Adds the error message to the field
                del cleaned_data["start_date_for_excavation"]
                
        
            
        return cleaned_data 
        #Return the data back to the form
        
    #A function that will print values in a format, when we email the form
    def as_string(self):
        return '''
                Please check Django admin page for this new submission ->
        
                Applicant name: %s\n
                Company: %s\n
                Excavate: %s\n
                Bore: %s\n
                Reason: %s\n
                Location: %s\n
                Start date: %s\n
                End date: %s\n
                ''' % (self.cleaned_data['applicant_name'],
                                            self.cleaned_data['company'],
                                            self.cleaned_data['excavate'],
                                            self.cleaned_data['bore'],
                                            self.cleaned_data['reason_for_excavation_or_boring'],
                                            self.cleaned_data['location_of_excavation_including_termination_points'],
                                            self.cleaned_data['start_date_for_excavation'],
                                            self.cleaned_data['projected_end_date_for_excavation'])        
        
    #Global settings for the model    
    class Meta:
        model = ExcavateModel #All fields come from the model 'ExcavateModel'
        exclude = ['reviewed_by','meeting_held_with_applicant','date_of_approval','server'] #These fields are not seen in the form (in the html page)
        #Changing date fields to look like date fields
        widgets = {
            'start_date_for_excavation' : forms.DateInput(attrs={'type': 'date'}),
            'projected_end_date_for_excavation' : forms.DateInput(attrs={'type': 'date'}),
        }
