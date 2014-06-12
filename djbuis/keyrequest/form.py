from django import forms
from models import Keys
from django.core.exceptions import ValidationError
from django.core import validators
import re

# Create your forms here.
class ModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)

    def clean_contact_number(self):
        data = self.cleaned_data['contact_number']
        if not re.match(r'^((?:1?[\s\-\.\/]?\(?(?:\d{3})\)?)?[\s\-\.\/]?\d{3}[\s\-\.\/]?\d{4}(?:\s?(?:x|ext|\.)?\s?\d{4})?)$', data):
            raise forms.ValidationError('Enter a valid phone number')
        return data
    
    def clean(self):
        cleaned_data = super(ModelForm, self).clean()

        reason = cleaned_data.get("reason")
        other = cleaned_data.get("other")

        if reason == "OTH" and other == "":
            msg = u"Please give a reason for picking \"other\""
            self._errors["other"] = self.error_class([msg])

            del cleaned_data["reason"]
            del cleaned_data["other"]
            return cleaned_data
    class Meta:
        model = Keys
        widgets = {
            'reason': forms.RadioSelect()
            }
        exclude = ('signature', 'signature1', 'signature2', 'signature3', 'signature4', 'chair_sig', 'dean_sig',  'date_completed',)
