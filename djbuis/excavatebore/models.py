from django.db import models
from django.core.exceptions import ValidationError #Added this so I could make validation functions here

#A simple test
def validate_boolean_must_be_true(value):
    if value == False:
        raise ValidationError('Value must be true')


class ExcavateModel(models.Model):
    
    #All of the fields in my form are below
    
    excavate = models.BooleanField() #Renders as a checkbox
    bore = models.BooleanField()
    
    applicant_name = models.CharField(blank=False,max_length=64) #'max_length' is the maximum number of characters allowed in this field
    company = models.CharField(blank=False,max_length=64) #'blank=False' means the field is required
    reason_for_excavation_or_boring = models.CharField(blank=False,max_length=200)
    location_of_excavation_including_termination_points = models.CharField(blank=False,max_length=200)
    start_date_for_excavation = models.DateField(blank=False,error_messages={'required': 'custom required message'}) #You can also put in error messages
    projected_end_date_for_excavation = models.DateField(error_messages={'required': 'custom required message','null':'custom required message', 'blank':'custom required message', 'invalid':'custom required message', 'invalid_choice':'custom required message'})
    reviewed_by = models.CharField(null=True,max_length=64) #'null=True' means the field can be null in the database
    meeting_held_with_applicant = models.BooleanField(default=True, validators=[validate_boolean_must_be_true]) #I added the validation function to this field
    date_of_approval = models.DateField(null=True)
    
    #Values in the database are the first word, second word is what the user sees
    STATUS = (
        ('stag', 'Staging Server'),
        ('prod', 'Production Server'),
    )

    server = models.CharField(max_length=4,choices=STATUS,default='stag') #Renders as a select box, with default being 'Staging Server' 
    
    #Here I set global options for this model
    class Meta:
        verbose_name = 'Excavate - Bore application' #I want to call it 'Excavate / Bore' in the django admin page
        verbose_name_plural = 'Excavate - Bore applications' #Plural version
        #db_table = 'excavate_app_excavatemodel'
    
#I make a proxy here because I want to (eventually) put this form, along with others, under a common header
class ExcavateProxy(ExcavateModel):
    class Meta:
        proxy = True
        app_label = 'Registrar' #The common header
        verbose_name = 'a' #What the form will show up as under the common header
        

