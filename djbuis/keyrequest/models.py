from django.db import models
from django import forms

#below you create the models that will be used to make forms in the form.py file
class OtherModel(models.Model):

    REASONS= (
        ("NEWE", 'New Employee'),
        ("NEWO", 'New Office or Facility Assignment'),
        ("LOCK", 'Lock Change'),        
        ("WORN", 'Worn Key Returned'),
        ("OTH", 'Other (please explain)'),
    )
    
    reason = models.CharField(choices=REASONS, max_length = 200, default = "NEWE")
    other = models.CharField(max_length = 400, blank=True)
    date_completed = models.DateField(blank=True)
    dean_sig = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    Date = models.DateField(auto_now_add=True)
    account = models.CharField(max_length=150)



class KeyModel(models.Model):
    
    key = models.ForeignKey(OtherModel)
    
    #Values in the database are the first word, second word is what the user sees
    BUILDINGS = (
        ("LIB", 'Library'),
        ("STRZ", 'Straz'),
        ("LNTZ", 'Lentz'),        
        ("JART", 'Johnson Art Center'),
        ("TARC", 'TARC'),
        ("CHPL", 'Chapel'),
        ("DNHT", 'Denhart Hall'),
        ("TARB", 'Tarble Hall'),
        ("MADR", 'Madrigrano Hall'),
        ("JOHN", 'Johnson Hall'),
        ("SWEN", 'Swenson Hall'),
        ("OAKS1", 'Oaks 1'),
        ("OAKS2", 'Oaks 2'),
        ("OAKS3", 'Oaks 3'),
        ("OAKS4", 'Oaks 4'),
        ("OAKS5", 'Oaks 5'),
        ("OAKS6", 'Oaks 6'),
    )
        
    building = models.CharField(choices=BUILDINGS, max_length=200, blank=False) #The choices field uses the choices outlined above to make a select list.
    room_number = models.PositiveIntegerField(max_length=5, blank=False) #'max_length' is the maximum number of characters allowed in this field
    key_code_if_known = models.CharField(max_length=100, blank=True)
    issued_to = models.CharField(max_length=100, blank=False)
    

