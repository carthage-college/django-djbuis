from django.db import models

# Create your models here.
class Maintenance(models.Model):
	building = models.CharField(max_length=20)
	floor = models.CharField(max_length=2)
	room = models.PositiveIntegerField()
	other_location_information = models.CharField(max_length=200, blank=True)
	description_of_service = models.CharField(max_length=200)
	name = models.CharField(max_length=50)
	campus_telephone = models.CharField(max_length=16)
	office = models.CharField(max_length=20)
	date_recieved = models.DateField(auto_now_add=True)
	date_completed = models.DateField(blank=True, null=True)
	repaired_by = models.CharField(max_length=50, blank=True, null=True)
	DELAY_CHOICES = (
		('parts ordered', 'Parts Ordered'),
		('not repairable', 'Not Repairable'),
		('referred to vendor', 'Referred to Vendor/Contractor'),
	)
	delay_due_to = models.CharField(choices=DELAY_CHOICES, max_length=30, blank=True, null=True)
	delayed_repair_scheduled = models.CharField(max_length=50, blank=True, null=True)
	departmental_charge = models.BooleanField()
	account_number = models.PositiveIntegerField(blank=True, null=True)
	comments = models.CharField(max_length=200, blank=True, null=True)
	def __unicode__(self):
		return self.name
	
class ProxyMaintenance(Maintenance):
	class Meta:
		proxy = True
		app_label = 'Business'
		verbose_name = 'Maintenance Form'
