#Include django.forms
from django import forms
from djbuis.phonemove.models import PhoneModel
from django.core.exceptions import ValidationError
from django.core import validators

# Create your forms here.
class PhoneForm(forms.ModelForm):    
    
    def __init__(self, *args, **kwargs):
        super(PhoneForm, self).__init__(*args, **kwargs)
        
        #Adding labels here
        self.fields['name'].label = "Name of User"
        self.fields['department'].label = "Department"
        self.fields['user_number'].label = "User\'s Phone Number or Extension"
        self.fields['request'].label = "What are you requesting?"
        self.fields['from_location'].label = "From Location"
        self.fields['to_location'].label = "To Location"
        self.fields['caller_id'].label = "New caller ID"
        self.fields['date_of_change'].label = "Date of service"
        self.fields['email'].label = "Email me the form after submitting"
        
        #Adding regex validators to fields
        self.fields['name'].validators = [validators.RegexValidator(regex='^[a-zA-Z\']+[a-zA-Z\-\s\']+$', message='Invalid name', code='bad name')]
        self.fields['department'].validators = [validators.RegexValidator(regex='^.+$', message='Not a valid department', code='bad department')]
        self.fields['user_number'].validators = [validators.RegexValidator(regex='^(\d{4}|\d{3}[\s\-\.]?\d{4}|1?[\s\-\.]?\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4}|NEW)$', message='Enter a phone number \"###-###-####\", \"###-###-#### x####\", \"####\"" or the word \"NEW\"', code='bad_phone')]
        
        #Adding these for now..
        self.fields['from_location'].validators = [validators.RegexValidator(regex='^.+$', message='Enter a \'from location\'', code='a')]
        self.fields['to_location'].validators = [validators.RegexValidator(regex='^.+$', message='Enter a \'to location\'', code='a')]
        self.fields['caller_id'].validators = [validators.RegexValidator(regex='^.+$', message='Enter a \'caller id\'', code='a')]
        
        #Custom error messages are here
        #you can replace 'required' with 'invalid' for invalid fields like so
        #
        # self.fields['name'].error_messages = {'required': 'Please fill in a name.','invalid':'This field is invalid'}
        self.fields['name'].error_messages = {'required': 'Please fill in a name.'}
        self.fields['department'].error_messages = {'required': 'Please fill in a department.'}
        self.fields['user_number'].error_messages = {'required': 'Please fill in a phone number.'}
        self.fields['request'].error_messages = {'required': 'Please select one of the answers below.'}
        self.fields['from_location'].error_messages = {'required': 'Please fill in a from location.'}
        self.fields['to_location'].error_messages = {'required': 'Please fill in a to location.'}
        self.fields['caller_id'].error_messages = {'required': 'Please fill in a caller id.'}
        self.fields['date_of_change'].error_messages = {'required': 'Please fill in a date of change.'}
    
    def clean(self):
        cleaned_data = self.cleaned_data #Grabs the clean data
        date_of_change = cleaned_data.get('date_of_change')
        
        if date_of_change == None or date_of_change == "":
            msg = u"Invalid or past date"
            self._errors['date_of_change'] = self.error_class([msg])
        else:  
            if date_of_change < datetime.date.today():
                msg2 = u"The date cannot be in the past!"
                self._errors["date_of_change"] = self.error_class([msg2]) #Adds the error message to the field
                del cleaned_data["date_of_change"]
        return cleaned_data
    
    #This function returns a string that will be sent in an email    
    def to_mail(self):
        
        #Must be 'cleaned_data' (ie. after validation)
        if self.cleaned_data['email'] == True:
            return "%s \n %s \n %s \n %s \n %s \n %s \n %s \n %s \n " % (self.cleaned_data['name'], self.cleaned_data['department'], self.cleaned_data['user_number'], self.cleaned_data['request'], self.cleaned_data['from_location'], self.cleaned_data['to_location'], self.cleaned_data['caller_id'], self.cleaned_data['date_of_change'])
    
    #Global options
    class Meta:
        model = PhoneModel #We are using the fields from the model 'Phone'
        widgets = { #Change the way the fields are displayed
            #'from_location': forms.Textarea(),
            #'to_location': forms.Textarea(),
            'email': forms.CheckboxInput(),
            'request': forms.RadioSelect(),
            'date_of_change': forms.DateInput(attrs={'type':'date'}) #This is a datepicker
        }
