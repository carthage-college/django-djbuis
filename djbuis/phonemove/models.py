from django.db import models
from django import forms
from django.forms.models import modelformset_factory

class Phone(models.Model):

    REASONS= (
        ("MOVE", 'Move'),
        ("ADD", 'Add'),
        ("REPL", 'Replacement'),
        ("CHNG", 'Change of Service'),
    )

    name = models.CharField(max_length=100, verbose_name="Name of User")
    department = models.CharField(max_length=200, verbose_name="Department")
    user_number = models.CharField(max_length=16, verbose_name="User\'s Phone Number or Extension")
    request = models.CharField(choices=REASONS, max_length=100, default="MOVE", verbose_name="What are you requesting?")
    from_location = models.CharField(max_length=500, verbose_name="From Location")
    to_location = models.CharField(max_length=500, verbose_name="To Location")
    caller_id = models.CharField(max_length=500, verbose_name="Caller ID Name Change or Add")
    date_of_change = models.DateField(verbose_name="Date of move, add, change")
    email = models.BooleanField(verbose_name="Check this box if you would like the form to be emailed to you upon completion.") #This is a checkbox field

    class Meta:
        verbose_name = 'Phone move application'
        verbose_name_plural = 'Phone move applications'
