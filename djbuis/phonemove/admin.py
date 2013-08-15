from django.contrib import admin
from djbuis.phonemove.models import Phone

'''def push_to_database(modeladmin, request, queryset):
	for item in queryset:
		FinprivRec.objects.using('productiondefault').get_or_create(, code_name=item.name)
		
push_to_database.short_description = "Approve for moving to another database"
'''
class Admin(admin.ModelAdmin):
	list_display = ('name', 'date_of_change')
	#actions = [push_to_database]
	
admin.site.register(Phone, Admin)
