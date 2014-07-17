from django.db import models
from django.core.exceptions import ValidationError #Added this so I could make validation functions here

#A simple test
def validate_boolean_must_be_true(value):
    if value == False:
        raise ValidationError('Value must be true')


class ExcavateModel(models.Model):
    
    EXCBORE = (
        ("EXC", 'Excavate'),
        ("BORE", 'Bore'),
        )
    
    excavate_bore = models.CharField(choices=EXCBORE, max_length=15)    
    applicant_name = models.CharField(blank=False,max_length=64) #'max_length' is the maximum number of characters allowed in this field
    phone = models.CharField(max_length=15)
    company = models.CharField(blank=False,max_length=64) #'blank=False' means the field is required
    reason = models.CharField(blank=False,max_length=200)
    location = models.CharField(blank=False,max_length=200)
    start_date = models.DateField(blank=False)
    end_date = models.DateField()
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
        

