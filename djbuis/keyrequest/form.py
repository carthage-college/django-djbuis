#Include django.forms
from django import forms
from django.core.exceptions import ValidationError #This is so we can make error messages
from django.core import validators #This is so we can use regex
from django.forms.formsets import BaseFormSet

from djbuis.keyrequest.models import KeyModel, OtherModel #Don't forget to import your models!

# Create your forms here.
class KeyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(KeyForm, self).__init__(*args, **kwargs)
        
        self.fields['building'].error_messages['required'] = 'Required'
        self.fields['room_number'].error_messages = {'required': 'Required', 'invalid': 'Use a whole number'}
        self.fields['key_code_if_known'].error_messages['required'] = 'Required'
        self.fields['issued_to'].error_messages['required'] = 'Required'
        
    class Meta:
        model = KeyModel
        exclude = ('key')
    
class OtherForm(forms.ModelForm):    
    #This is needed if you want to add error messages, labels or additional validation for fields
    def __init__(self, *args, **kwargs):
        super(OtherForm, self).__init__(*args, **kwargs)
        
        self.fields['name'].validators = [validators.RegexValidator(regex='^[a-zA-Z\']+[a-zA-Z\-\s\']+$', message='Invalid characters in name', code='bad_name')]
        self.fields['contact_number'].validators = [validators.RegexValidator(regex='^(\d{4}|\d{3}[\s\-\.]?\d{4}|1?[\s\-\.]?\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4})$', message='Enter a valid phone number', code='bad_phone')]
        self.fields['account'].label = "Account to Charge"

    #Another way to include custom validation
    def clean(self):                                                                                                                                      
        cleaned_data = super(OtherForm, self).clean() #Grabs the clean data

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
        model = OtherModel #All fields come from the model 'OtherModel'
        widgets = {
            'reason': forms.RadioSelect() #Turns the select drop down into a radio button select
            }
        exclude = ('dean_sig', 'date_completed',) #These fields are not seen in the form (in the html page)
        
class RequiredFormSet(BaseFormSet):
    def __init__(self, *args, **kwargs):
        super(RequiredFormSet, self).__init__(*args, **kwargs)
        
        self.forms[0].empty_permitted = False
