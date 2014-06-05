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
        if not re.match(r'^1?-?\(?\d{3}\)?-?\d{3}-?\d{4}$', data):
            raise forms.ValidationError('Enter a valid phone number')
        return data
    
    def clean(self):
        cleaned_data = super(ModelForm, self).clean()

        reason = cleaned_data.get("reason")
        other = cleaned_data.get("other")

        building = cleaned_data.get("building")
        room_number = cleaned_data.get("room_number")
        key_code_if_known = cleaned_data.get("key_code_if_known")
        issued_to = cleaned_data.get("issued_to")

        if reason == "OTH" and other == "":
            msg = u"Please give a reason for picking \"other\""
            self._errors["other"] = self.error_class([msg])

            del cleaned_data["reason"]
            del cleaned_data["other"]

        if building == "":
            msg = u"You did not fill in the first field of this column."
            self._errors["building"] = self.error_class([msg])
            del cleaned_data["building"]

        if room_number == "":
            msg = u"You did not fill in the first field of this column."
            self._errors["room_number"] = self.error_class([msg])
            del cleaned_data["room_number"]

        if key_code_if_known == "":
            msg = u"You did not fill in the first field of this column."
            self._errors["key_code_if_known"] = self.error_class([msg])
            del cleaned_data["key_code_if_known"]

        if issued_to == "":
            msg = u"You did not fill in the first field of this column."
            self._errors["issued_to"] = self.error_class([msg])
            del cleaned_data["issued_to"]

        return cleaned_data
    class Meta:
        model = Keys
        widgets = {
            'reason': forms.RadioSelect()
            }
        exclude = ('signature', 'signature1', 'signature2', 'signature3', 'signature4', 'chair_sig', 'dean_sig',  'date_completed',)
