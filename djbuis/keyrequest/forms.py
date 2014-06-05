from django import forms
from django.conf import settings
import datetime

from djtools.fields import REQ_CSS

BUILDINGS = (
    ("-----", "-----"),
    ("LIB", 'Library'),
    ("STRZ", 'Straz'),
    ("LNTZ", 'Lentz'),
    ("JART", 'Johnson Art Center'),
    ("TARC", 'TARC'),
    ("CHPL", 'Chapel'),
    ("DNHT", 'Denhart Hall'),
    ("TARB", 'Tarble Hall'),
    ("MADR", 'Madrigrano Hall'),
    ("JOHN", 'Johnson Hall'),
    ("SWEN", 'Swenson Hall'),
    ("OAKS1", 'Oaks 1'),
    ("OAKS2", 'Oaks 2'),
    ("OAKS3", 'Oaks 3'),
    ("OAKS4", 'Oaks 4'),
    ("OAKS5", 'Oaks 5'),
    ("OAKS6", 'Oaks 6'),
    )
REASONS= (
    ("NEWE", 'New Employee'),
    ("NEWO", 'New Office or Facility Assignment'),
    ("LOCK", 'Lock Change'),
    ("WORN", 'Worn Key Returned'),
    ("OTH", 'Other (please explain)'),
    )

class KeyForm(forms.Form):
    building = forms.ChoiceField(
        label = "Building",
        choices = BUILDINGS
    )
    room_number = forms.CharField(
        label = "Room Number",
        required = False
    )
    key_code_if_known = forms.CharField(
        label = "Key Code",
        required = False
    )
    issued_to = forms.CharField(
        label = "Issued To:",
        required = False
    )
    signature = forms.CharField(
        required = False,
        widget = forms.HiddenInput()
    )

    building1 = forms.ChoiceField(
        label = "Building",
        choices = BUILDINGS
    )
    room_number1 = forms.CharField(
        label = "Room Number",
        required = False
    )
    key_code_if_known1 = forms.CharField(
        label = "Key Code",
        required = False
    )
    issued_to1 = forms.CharField(
        label = "Issued To:",
        required = False
    )
    signature1 = forms.CharField(
        required = False,
        widget = forms.HiddenInput()
    )

    building2 = forms.ChoiceField(
        label = "Building",
        choices = BUILDINGS
    )
    room_number2 = forms.CharField(
        label = "Room Number",
        required = False
    )
    key_code_if_known2 = forms.CharField(
        label = "Key Code",
        required = False
    )
    issued_to2 = forms.CharField(
        label = "Issued To:",
        required = False
    )
    signature2 = forms.CharField(
        required = False,
        widget = forms.HiddenInput()
    )

    building3 = forms.ChoiceField(
        label = "Building",
        choices = BUILDINGS
    )
    room_number3 = forms.CharField(
        label = "Room Number",
        required = False
    )
    key_code_if_known3 = forms.CharField(
        label = "Key Code",
        required = False
    )
    issued_to3 = forms.CharField(
        label = "Issued To:",
        required = False
    )
    signature3 = forms.CharField(
        required = False,
        widget = forms.HiddenInput()
    )

    building4 = forms.ChoiceField(
        label = "Building",
        choices = BUILDINGS
    )
    room_number4 = forms.CharField(
        label = "Room Number",
        required = False
    )
    key_code_if_known4 = forms.CharField(
        label = "Key Code",
        required = False
    )
    issued_to4 = forms.CharField(
        label = "Issued To:",
        required = False
    )
    signature4 = forms.CharField(
        required = False,
        widget = forms.HiddenInput()
    )

    reason = forms.CharField(
        label = "Reason:",
        widget = forms.RadioSelect(choices = REASONS, attrs=REQ_CSS)
    )
    other = forms.CharField(
        max_length = 100,
        required = False
    )
    date_completed = forms.DateField(
        widget = forms.HiddenInput,
        initial = datetime.date.today
    )
    chair_sig = forms.CharField(
        required = False,
        widget = forms.HiddenInput()
    )
    dean_sig = forms.CharField(
        required = False,
        widget = forms.HiddenInput()
    )
    name = forms.CharField(
        label = "Name:"
    )
    contact_number = forms.CharField(
        label = "Contact Number:"
    )
    account = forms.CharField(
        label = "Account to Charge:"
    )

    def clean(self):
        cleaned_data = super(KeyForm, self).clean()

        reason = cleaned_data.get("reason")
        other = cleaned_data.get("other")

        building = cleaned_data.get("building")
        building1 = cleaned_data.get("building1")
        building2 = cleaned_data.get("building2")
        building3 = cleaned_data.get("building3")
        building4 = cleaned_data.get("building4")
        room_number = cleaned_data.get("room_number")
        key_code_if_known = cleaned_data.get("key_code_if_known")
        issued_to = cleaned_data.get("issued_to")

        if reason == "OTH" and other == "":
            msg = u"Please give a reason for picking \"other\""
            self._errors["other"] = self.error_class([msg])

            del cleaned_data["reason"]
            del cleaned_data["other"]

        if building == "-----":
            msg = u"You did not fill in the buidling column."
            self._errors["building"] = self.error_class([msg])
            del cleaned_data["building"]

        if room_number == "":
            msg = u"You did not fill in the room number column."
            self._errors["room_number"] = self.error_class([msg])
            del cleaned_data["room_number"]

        if key_code_if_known == "":
            msg = u"You did not fill in the key code column."
            self._errors["key_code_if_known"] = self.error_class([msg])
            del cleaned_data["key_code_if_known"]

        if issued_to == "":
            msg = u"You did not fill in the issued to column."
            self._errors["issued_to"] = self.error_class([msg])
            del cleaned_data["issued_to"]

        return cleaned_data













