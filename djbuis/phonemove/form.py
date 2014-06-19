import datetime, re
from django import forms
from models import Phone
from django.core.exceptions import ValidationError
from django.core import validators

# Create your forms here.
class ModelForm(forms.ModelForm):    
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
    
    def clean_name(self):
        data = self.cleaned_data['name']
        if not re.match(r'^((?:[a-zA-Z]+\s?){1,2}[a-zA-Z]+)$', data):
            raise forms.ValidationError('This name is invalid. Check for special characters or extra spaces.')
        return data
    def clean_department(self):
        data = self.cleaned_data['department']
        if not re.match(r'^((?:[a-zA-Z]+\s?)+[a-zA-Z]+)$', data):
            raise forms.ValidationError('This department name is invalid. Check for special characters or extra spaces.')
        return data
    def clean_user_number(self):
        data = self.cleaned_data['user_number']
        if not re.match(r'^((?:1?[\s\-\.\/]?\(?(?:\d{3})\)?)?[\s\-\.\/]?\d{3}[\s\-\.\/]?\d{4}(?:\s?(?:x|ext|\.)?\s?\d{4})?|NEW)$', data):
            raise forms.ValidationError('You did not enter a valid phone number or the word "NEW"')
    def clean_request(self):
        data = self.cleaned_data['request']
        if not re.match(r'^(MOVE|ADD|REPL|CHNG)$', data):
            raise forms.ValidationError('You have not selected a valid value.')
        return data
    def clean_from_location(self):
        data = self.cleaned_data['from_location']
        if not re.match(r'^((?:[\w]+[\s\.\!\$\(\)\/\,\:\;\?\'\-]+)+[\w\.\!\?\)]+)$', data):
            raise forms.ValidationError('Invalid location. Alphanumeric characters and spaces only.')
        return data
    def clean_to_location(self):
        data = self.cleaned_data['to_location']
        if not re.match(r'^((?:[\w]+[\s\.\!\$\(\)\/\,\:\;\?\'\-]+)+[\w\.\!\?\)]+)$', data):
            raise forms.ValidationError('Invalid location. Alphanumeric characters and spaces only.')
        return data
    def clean_caller_id(self):
        data = self.cleaned_data['caller_id']
        if not re.match(r'^((?:[a-zA-Z]+\s?)+[a-zA-Z]+)$', data):
            raise forms.ValidationError('Invalid caller id. No special characters or numbers.')
        return data
    def clean_date_of_change(self):
        data = self.cleaned_data['date_of_change']
        if data < datetime.date.today():
            raise forms.ValidationError('The date cannot be in the past!')
        return data
    
    def to_mail(self):
        if self.cleaned_data['email'] == True:
            return '''%(name)s
            %(department)s
            %(user_number)s
            %(request)s
            %(from_location)s
            %(to_location)s
            %(caller_id)s
            %(date_of_change)s''' % self.cleaned_data
            
    class Meta:
        model = Phone
        widgets = {
            'from_location': forms.Textarea(),
            'to_location': forms.Textarea(),
            'email': forms.CheckboxInput(),
            'request': forms.RadioSelect(),
            'date_of_change': forms.DateInput(attrs={'type':'date'})
            }
