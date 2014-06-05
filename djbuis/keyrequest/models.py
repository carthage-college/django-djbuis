from django.db import models
from django import forms
from django.forms.models import modelformset_factory

class Keys(models.Model):

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
    REASONS= (
        ("NEWE", 'New Employee'),
        ("NEWO", 'New Office or Facility Assignment'),
        ("LOCK", 'Lock Change'),
        ("WORN", 'Worn Key Returned'),
        ("OTH", 'Other (please explain)'),
        )

    building = models.CharField(choices=BUILDINGS, max_length=50, verbose_name="Building")
    room_number = models.PositiveIntegerField(max_length=5, verbose_name="Room Number")
    key_code_if_known = models.CharField(max_length=100, verbose_name="Key Code")
    issued_to = models.CharField(max_length=100, verbose_name="Issued to")
    signature = models.CharField(max_length=100, blank=True)
    building1 = models.CharField(choices=BUILDINGS, max_length=200, blank=True)
    room_number1 = models.IntegerField(max_length=20000, blank=True, null=True)
    key_code_if_known1 = models.CharField(max_length=100, blank=True)
    issued_to1 = models.CharField(max_length=100, blank=True)
    signature1 = models.CharField(max_length=100, blank=True)
    building2 = models.CharField(choices=BUILDINGS, max_length=200, blank=True)
    room_number2 = models.IntegerField(max_length=20000, blank=True, null=True)
    key_code_if_known2 = models.CharField(max_length=100, blank=True)
    issued_to2 = models.CharField(max_length=100, blank=True)
    signature2 = models.CharField(max_length=100, blank=True)
    building3 = models.CharField(choices=BUILDINGS, max_length=200, blank=True)
    room_number3 = models.IntegerField(max_length=20000, blank=True, null=True)
    key_code_if_known3 = models.CharField(max_length=100, blank=True)
    issued_to3 = models.CharField(max_length=100, blank=True)
    signature3 = models.CharField(max_length=100, blank=True)
    building4 = models.CharField(choices=BUILDINGS, max_length=200, blank=True)
    room_number4 = models.IntegerField(max_length=20000, blank=True, null=True)
    key_code_if_known4 = models.CharField(max_length=100, blank=True)
    issued_to4 = models.CharField(max_length=100, blank=True)
    signature4 = models.CharField(max_length=100, blank=True)
    reason = models.CharField(choices=REASONS, default = "NEWE", max_length=50,  verbose_name="Reason:")
    other = models.CharField(max_length = 500, blank=True)
    date_completed = models.DateField(blank=True)
    chair_sig = models.CharField(max_length=100, blank=True)
    dean_sig = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, verbose_name="Name:")
    contact_number = models.CharField(max_length=15, verbose_name="Contact Number:")
    Date = models.DateField(auto_now_add=True)
    account = models.CharField(max_length=150, verbose_name="Account to Charge:")
