#Include django.forms
import datetime
from django import forms
from django.core import validators
from djbuis.excavatebore.models import ExcavateModel #Include the model that goes with this form
from django.contrib.admin import widgets #Import this if you want to change the layout of certain fields

class ExcavateForm(forms.ModelForm):

    #This is needed if you want to add error messages, labels or additional validation for fields
    def __init__(self, *args, **kwargs):
        super(ExcavateForm, self).__init__(*args,**kwargs)
        
        #I am adding error messages if neither field has any value in it or if it is invalid
        self.fields['start_date_for_excavation'].error_messages = {'required': 'Use this format:mm/dd/yyyy','invalid': 'Try this format:mm/dd/yyyy'}
        self.fields['projected_end_date_for_excavation'].error_messages = {'required': 'Use this format:mm/dd/yyyy','invalid': 'Try this format:mm/dd/yyyy'}
        
        self.fields['applicant_name'].validators = [validators.RegexValidator(regex='^[a-zA-Z\']+[a-zA-Z\-\s\']+$', message='Not a valid name', code='a')]
        self.fields['company'].validators = [validators.RegexValidator(regex='^.+$', message='Not a valid company', code='a')]
        self.fields['reason_for_excavation_or_boring'].validators = [validators.RegexValidator(regex='^.+$', message='Please remove invalid characters', code='a')]
        self.fields['location_of_excavation_including_termination_points'].validators = [validators.RegexValidator(regex='^.+$', message='Please remove invalid characters', code='a')]
        
    #Another option to include validation
    def clean(self):
        cleaned_data = self.cleaned_data #Grabs the clean data
        excavate = cleaned_data.get("excavate")
        bore = cleaned_data.get("bore")
        
        if excavate == False and bore == False:
            msg = u"Please select either 'Excavate' or 'Bore'"
            self._errors["excavate"] = self.error_class([msg]) #Adds the error message to the field
            self._errors["bore"] = self.error_class([msg]) #Adds the error message to the field
            
            del cleaned_data["excavate"] #Django told me to do this?
            del cleaned_data["bore"]
            
        date1 = cleaned_data.get('start_date_for_excavation')
        date2 = cleaned_data.get('projected_end_date_for_excavation')
        
        
        if date1 == None or date1 == "":
            msg = u"Invalid or past date"
            self._errors['start_date_for_excavation'] = self.error_class([msg])
        else:  
            if date1 < datetime.date.today():
                msg2 = u"The date cannot be in the past!"
                self._errors["start_date_for_excavation"] = self.error_class([msg2]) #Adds the error message to the field
                del cleaned_data["start_date_for_excavation"]
                
        if date2 == None or date2 == "":
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
