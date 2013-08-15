from django.db import models

from django.core.exceptions import ValidationError

def validate_boolean_must_be_true(value):
    if value == False:
        raise ValidationError('Value must be true')


# Create your models here.
class ExcavateModel(models.Model):
	
    excavate = models.BooleanField()
    bore = models.BooleanField()
	
    applicant_name = models.CharField(blank=False,max_length=64)
    company = models.CharField(blank=False,max_length=64)
    reason_for_excavation_or_boring = models.CharField(blank=False,max_length=200)
    location_of_excavation_including_termination_points = models.CharField(blank=False,max_length=200)
    start_date_for_excavation = models.DateField(blank=False,error_messages={'required': 'custom required message'})
    projected_end_date_for_excavation = models.DateField(error_messages={'required': 'custom required message','null':'custom required message', 'blank':'custom required message', 'invalid':'custom required message', 'invalid_choice':'custom required message'})
    reviewed_by = models.CharField(null=True,max_length=64)
    meeting_held_with_applicant = models.BooleanField(default=True, validators=[validate_boolean_must_be_true])
    date_of_approval = models.DateField(null=True)
	
    STATUS = (
        ('stag', 'Staging Server'),
        ('prod', 'Production Server'),
    )

    server = models.CharField(max_length=4,choices=STATUS,default='stag')
	
    class Meta:
        verbose_name = 'Excavate / Bore'
        verbose_name_plural = 'Excavate / Bore'
		#db_table = 'excavate_app_excavatemodel'
	
class ExcavateProxy(ExcavateModel):
	class Meta:
		proxy = True
		#app_label = 'Registrar'
		#verbose_name = 'a'
		

