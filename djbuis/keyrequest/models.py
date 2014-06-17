from django.db import models

class Info(models.Model):
    REASONS= (
        ("NEWE", 'New Employee'),
        ("NEWO", 'New Office or Facility Assignment'),
        ("LOCK", 'Lock Change'),
        ("WORN", 'Worn Key Returned'),
        ("OTH", 'Other (please explain)'),
        )
    signature = models.CharField(max_length=100, blank=True)
    reason = models.CharField(choices=REASONS, default = "NEWE",
                                max_length=50,
                                verbose_name="Reason:")
    other = models.CharField(max_length = 500, blank=True)
    date_completed = models.DateField(blank=True)
    chair_sig = models.CharField(max_length=100, blank=True)
    dean_sig = models.CharField(max_length=100, blank=True)
    name = models.CharField(max_length=100, verbose_name="Name:")
    contact_number = models.CharField(max_length=15,
                                verbose_name="Contact Number:")
    Date = models.DateField(auto_now_add=True)
    account = models.CharField(max_length=150,
                                verbose_name="Account to Charge:")
    
class KeyInfo(models.Model):
    key = models.ForeignKey(Info)
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
    building = models.CharField(choices=BUILDINGS, max_length=50,
                                verbose_name="Building")
    room_number = models.PositiveIntegerField(max_length=5,
                                verbose_name="Room Number")
    key_code_if_known = models.CharField(max_length=100,
                                verbose_name="Key Code")
    issued_to = models.CharField(max_length=100,
                                verbose_name="Issued to")

