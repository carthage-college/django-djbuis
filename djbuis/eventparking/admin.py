from django.contrib import admin
from djbuis.eventparking.models import Parking, ProxyParking

class FormAdmin(admin.ModelAdmin):
	readonly_files = ('date_recieved')
	
admin.site.register(ProxyParking, FormAdmin)
