#Include django.forms
import datetime, re
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
           
    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if not re.match(r'^((?:1?[\s\-\.\/]?\(?(?:\d{3})\)?)?[\s\-\.\/]?\d{3}[\s\-\.\/]?\d{4}(?:\s?(?:x|ext|\.)?\s?\d{4})?)$', data):
            raise forms.ValidationError('Enter a valid phone number')
        return data
    
    def clean(self):
        cleaned_data = self.cleaned_data
        test = cleaned_data.get('event_date')
        
        if not test:
            msg = u"Invalid date"
            self._errors['event_date'] = self.error_class([msg])
        else:
            if test < datetime.date.today():
                msg2 = u"The date cannot be in the past"
                self._errors["event_date"] = self.error_class([msg2]) #Adds the error message to the field
                del cleaned_data["event_date"]
            
        return cleaned_data
           

    #A function that will print values in a format, when we email the form
    def as_string(self):
        return '''Please check Django admin page for this new submission ->
        
                Event name: %(event_name)s\n
                Event location: %(event_location)s\n
                Event time: %(event_time)s\n
                Event date: %(event_date)s\n
                Crowd estimate: %(crowd_estimate)s\n
                Contact person: %(contact_person)s\n
                Phone number: %(phone_number)s\n''' % (self.cleaned_data)

    #Global options for the form class    
    class Meta:
        model = Parking #Use all of the fields from Parking 
        exclude = ['parking_arrangements_required','date_completed'] #Exclude these fields from the form
        widgets = { #Changing the display of certain elements
            'event_date': forms.DateInput(attrs={'type': 'date'}), #Date picker
            'event_time': forms.TimeInput(attrs={'type': 'time'}),
            #'crowd_estimate': forms.TextInput(attrs={'type': 'number'}), #This is a number picker
            'phone_number': forms.TextInput(attrs={'maxlength': 16}),
        }
