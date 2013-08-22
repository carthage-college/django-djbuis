from django.db import models

# Create your models here.
class Parking(models.Model):
	
	#All of my fields for the form
	event_date = models.DateField() #Is a date field
	event_time = models.TimeField() #Is a time field
	crowd_estimate = models.PositiveIntegerField() #Only allows for positive numbers
	event_name = models.CharField(max_length=200) #'max_length' is a required field for (most) all forms
	event_location = models.CharField(max_length=200)
	contact_person = models.CharField(max_length=50)
	phone_number = models.CharField(max_length=16)
	parking_arrangements_required = models.CharField(max_length=200, blank=True, null=True) #'blank=True' allows for this field to remain blank
	date_recieved = models.DateField(auto_now_add=True) #Automatically adds the date to the current day as well as makes this field invisible
	date_completed = models.DateField(blank=True, null=True) #'null=True' means the data member can be represented as null in the database table
	
	#Defines how the model will represent itself in the admin page
	def __unicode__(self):
		return self.event_name

#A proxy class so we can have this model under a different header in the database
class ProxyParking(Parking):
	class Meta:
		proxy = True #Required for proxy classes
		#app_label = 'Business'
		verbose_name = 'Event Parking Form' #How the model will be represented in the database
