from django.db import models

# Create your models here.
class Parking(models.Model):
	event_date = models.DateField()
	event_time = models.TimeField()
	crowd_estimate = models.PositiveIntegerField()
	event_name = models.CharField(max_length=200)
	event_location = models.CharField(max_length=200)
	contact_person = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=16)
	parking_arrangements_required = models.CharField(max_length=200, blank=True, null=True)
	date_recieved = models.DateField(auto_now_add=True)
	date_completed = models.DateField(blank=True, null=True)
	def __unicode__(self):
		return self.event_name
	
class ProxyParking(Parking):
	class Meta:
		proxy = True
		app_label = 'Business'
		verbose_name = 'Event Parking Form'
