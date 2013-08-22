from django.db import models

#My model is called 'Phone'
class PhoneModel(models.Model):

	REASONS= (
		("MOVE", 'Move'),
		("ADD", 'Add'),
		("REPL", 'Replacement'),		
		("CHNG", 'Change of Service'),
	)
	
	#All my fields in the form

	name = models.CharField(max_length=100)
	department = models.CharField(max_length=200)
	user_number = models.CharField(max_length=15)
	request = models.CharField(choices=REASONS, max_length=100, default="MOVE") #This renders as a select box
	from_location = models.CharField(max_length=500)
	to_location = models.CharField(max_length=500)
	caller_id = models.CharField(max_length=500)
	date_of_change = models.DateField()
	email = models.BooleanField() #This is a checkbox field
