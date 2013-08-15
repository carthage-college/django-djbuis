from django.contrib import admin

from djbuis.excavatebore.models import ExcavateModel, ExcavateProxy
from django.contrib import messages

def push_to_production(modeladmin, request, queryset):
	push_to_production.short_description = 'Push to production server'
	
	
	#for each in queryset:
		
	#	(obj, created) = ExcavateAppExcavatemodel.objects.using('default2').get_or_create(id=127,excavate=each.excavate,bore=each.bore,applicant_name=each.applicant_name,company=each.company,reason_for_excavation_or_boring=each.reason_for_excavation_or_boring,location_of_excavation_including_termination_points=each.location_of_excavation_including_termination_points,start_date_for_excavation=each.start_date_for_excavation,projected_end_date_for_excavation=each.projected_end_date_for_excavation,reviewed_by=each.reviewed_by,meeting_held_with_applicant=each.meeting_held_with_applicant,date_of_approval=each.date_of_approval,server=each.server)
	#	if not obj.excavate or not obj.bore:
	#		messages.error(request, 'Form from %s : %s, has not chosen \'Excavate\' or \'Bore\'' % (obj.applicant_name, obj.company))
	#	elif obj.reviewed_by == None:
	#		messages.error(request, 'Form from %s : %s, has no data for \'Reviewed by\'' % (obj.applicant_name, obj.company))
	#	elif not obj.meeting_held_with_applicant:
	#		messages.error(request, 'Form from %s : %s, needs to have \'Meeting held with applicant\' checked' % (obj.applicant_name, obj.company))
	#	elif obj.date_of_approval == "":
	#		#You can also use warning, debug, info and success in place of error
	#		messages.error(request,'Form from %s : %s, has no data for \'Date of approval\'' % (obj.applicant_name, obj.company))
	#	else:
	#		queryset.update(server='prod')
	#		obj.save()
	#		messages.success(request, 'Request from %s : %s, has been copied to the production server' % (obj.applicant_name, obj.company))
			

class ExcavateAdmin(admin.ModelAdmin):
	search_fields = ['company']
	list_display = ('applicant_name','company','excavate','bore','server')
	actions = [push_to_production]
	fieldsets = (
		('Permit type', {
			'fields': ('excavate','bore')
		}),
		('Application information', {
			'classes': ('collapse',),
			'fields': ('applicant_name','company')
		}),
		('Project information', {
			'classes': ('collapse',),
			'fields': ('reason_for_excavation_or_boring','location_of_excavation_including_termination_points','start_date_for_excavation','projected_end_date_for_excavation')
		}),
		('Administrator action', {
			'fields': ('reviewed_by','meeting_held_with_applicant','date_of_approval','server')
		})
	)
	list_filter = ('server','excavate','bore','company')
	readonly_fields = ('excavate','bore','server')

#admin.site.register(ExcavateProxy)	
admin.site.register(ExcavateModel, ExcavateAdmin)

