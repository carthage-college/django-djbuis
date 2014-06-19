from django import forms
from djbuis.keyrequest.models import KeyInfo, Info
from django.core.exceptions import ValidationError
from django.core import validators
import re

# Create your forms here.
class InfoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(InfoForm, self).__init__(*args, **kwargs)

    def clean_contact_number(self):
        data = self.cleaned_data['contact_number']
        if not re.match(r'^((?:1?[\s\-\.\/]?\(?(?:\d{3})\)?)?[\s\-\.\/]?\d{3}[\s\-\.\/]?\d{4}(?:\s?(?:x|ext|\.)?\s?\d{4})?)$', data):
            raise forms.ValidationError('Enter a valid phone number')
        return data
    
    def clean_name(self):
        data = self.cleaned_data['name']
        if not re.match(r'^((?:[a-zA-Z]+\s?){1,2}[a-zA-Z]+)$', data):
            raise forms.ValidationError('Enter a name with no special characters')
        return data
    
    def clean_account(self):
        data = self.cleaned_data['account']
        if not re.match(r'^((?:[a-zA-Z\s?\.?]+)[a-zA-Z]+)$', data):
            raise forms.ValidationError('Enter an account with no special characters.')
        return data
    
    def clean(self):
        cleaned_data = super(InfoForm, self).clean()

        reason = cleaned_data.get("reason")
        other = cleaned_data.get("other")

        if reason == "OTH" and other == "":
            msg = u"Please give a reason for picking \"other\""
            self._errors["other"] = self.error_class([msg])

            del cleaned_data["reason"]
            del cleaned_data["other"]
            return cleaned_data
        return self.cleaned_data
    
    class Meta:
        model = Info
        widgets = {'reason' : forms.RadioSelect}
        exclude = ('signature', 'signature1', 'signature2', 'signature3', 'signature4', 'chair_sig', 'dean_sig',  'date_completed',)

class KeyForm(forms.Form):
    BUILDINGS = (
        ("CHPL", 'Chapel'),
        ("DNHT", 'Denhart Hall'),
        ("JART", 'Johnson Art Center'),
        ("JOHN", 'Johnson Hall'),
        ("LNTZ", 'Lentz'),
        ("LIB", 'Library'),
        ("MADR", 'Madrigrano Hall'),
        ("OAKS1", 'Oaks 1'),
        ("OAKS2", 'Oaks 2'),
        ("OAKS3", 'Oaks 3'),
        ("OAKS4", 'Oaks 4'),
        ("OAKS5", 'Oaks 5'),
        ("OAKS6", 'Oaks 6'),
        ("STRZ", 'Straz'),
        ("SWEN", 'Swenson Hall'),
        ("TARB", 'Tarble Hall'),
        ("TARC", 'TARC'),
        )
    building = forms.ChoiceField(widget = forms.Select, choices=BUILDINGS)
    room_number = forms.IntegerField()
    key_code_if_known = forms.CharField()
    issued_to = forms.CharField()