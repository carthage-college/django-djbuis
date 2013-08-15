from django.contrib import admin
from djbuis.maintenance.models import Maintenance, ProxyMaintenance

class FormAdmin(admin.ModelAdmin):
	readonly_fields = ('date_recieved',)
	
admin.site.register(ProxyMaintenance, FormAdmin)
