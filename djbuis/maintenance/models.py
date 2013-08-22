from django.db import models

# Create your models here.
class Maintenance(models.Model):
	
	#All my fields for the form
	
	building = models.CharField(max_length=20)
	floor = models.CharField(max_length=2)
	room = models.CharField() #Only allows digits, no negatives
	other_location_information = models.CharField(max_length=200, blank=True) #with 'blank=True' you can leave these fields blank
	description_of_service = models.CharField(max_length=200)
	name = models.CharField(max_length=50)
	campus_telephone = models.CharField(max_length=16)
	office = models.CharField(max_length=20)
	date_recieved = models.DateField(auto_now_add=True) #Automatically sets the date to the current day, and IS invisible in the form
	date_completed = models.DateField(blank=True, null=True) #'null=True' can allow null values in the database for this field
	repaired_by = models.CharField(max_length=50, blank=True, null=True)
	DELAY_CHOICES = (
		('parts ordered', 'Parts Ordered'),
		('not repairable', 'Not Repairable'),
		('referred to vendor', 'Referred to Vendor/Contractor'),
	)
	delay_due_to = models.CharField(choices=DELAY_CHOICES, max_length=30, blank=True, null=True) #This renders as a select field
	delayed_repair_scheduled = models.CharField(max_length=50, blank=True, null=True)
	departmental_charge = models.BooleanField() #Renders as a checkbox
	account_number = models.PositiveIntegerField(blank=True, null=True)
	comments = models.CharField(max_length=200, blank=True, null=True)
	
	#How the model will be displayed
	def __unicode__(self):
		return self.name #We will see the 'name' field if we ever see this model

#Proxy class is used to create forms under a same header in the admin page
class ProxyMaintenance(Maintenance):
	class Meta:
		proxy = True #Need this for a proxy
		app_label = 'Business' #The 'header' this form exists under
		verbose_name = 'Maintenance Form' #The name that will appear under the header
