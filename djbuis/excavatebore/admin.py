#admin.py is where we create 'actions' that users can do to entries
#within this app, excavatebore, as well as settings to change how
#we view entries within 'excavatebore'

#'admin' - necessary to change view settings when viewing an 'excavatebore' object
#'messages' - necessary to change success/fail messages when performing an action to an 'excavatebore' object
from django.contrib import admin, messages
from djbuis.excavatebore.models import ExcavateModel, ExcavateProxy

#This is an 'action' a user can perform to a 'excavatebore' object
def push_to_production(modeladmin, request, queryset):
    push_to_production.short_description = 'Push to production server' #What the user sees
    
    # This is the bulk of moving data from the development to production databases
    #
    # *Understand this first - The data that exists in the form will be moved to separate
    # tables in the production server. Some fields might be moved to table 'A', others to table
    # 'B', and the rest might go to table 'C'. 
    # 
    # Steps to accomplish this:
    # 1) Find all of the tables where your data will be moving when it goes to the production
    # server. 
    #
    # 2) Download MySQLWorkbench and make copies of the tables on your local machine you found in step 1.
    # Be sure to copy the structure of the table exactly as found on the production server (including the name of the table)
    #
    # 3) Run this command and be sure 'newmodels.py' has been created in your project
    # (Run the command while within the 'root' project folder on your local machine. This
    # assumes you have been developing the form on your local machine)
    #       python manage.py inspectdb --database=default2 > newmodels.py
    #
    #   *Note: 'default2' is the name of your database where you have created the tables in
    #   step 2. This database should be a copy of the production database on the server (at the very least a copy of the tables you will need from step 1)
    #   This is found in the project's 'settings.py' file
    #
    # 4) On the top of this page, import the 'newmodels.py' file
    #
    # 5) Look in 'newmodels.py', you will see a bunch of classes. Each class represents a 
    # table. Now look at the fields in each class. For the below sample code, assume you had two classes
    # in 'newmodels.py' named 'table_one' and 'table_two'
    #
    #   'table_one' has these fields:
    #       id, name, tel
    #
    #   'table_two' has these fields:
    #       id, address
    #
    #   Also assume that your form has these fields:
    #       my_id, form, phone_number
    #
    # 6) For each class, use some code like below to save the data to your production database (keep this code in the function this comment is in)
    # *Note: replace 'default2' with the name YOU used for your production database (in 'settings.py')
    # *Note: feel free to un-comment the code below and make changes you need, you can keep these comments for reference
    # *Note: .get_or_create() makes an object if one is not found or updates an existing one if found
    # *Note: 'created' is a boolean that is true if an object was created from .get_or_create()
    # *Note: .save() saves the data to the production server
    # *Note: parameters within .get_or_create() are ... .get_or_create(field_from_newmodels.py=each.field_in_my_form)
    #
    #   for each in queryset: #Loops through all instances of the form object
    #       (obj, created) = table_one.objects.using('default2').get_or_create(id=each.my_id,name=each.name,tel=each.phone_number)
    #       obj.save()
    #       (obj, created) = table_two.objects.using('default2').get_or_create(id=each.my_id,address=each.address)
    #       if not obj.address:
    #           #You can also use 'warning', 'debug', 'info' and 'success' in place of 'error'
    #           messages.error(request, 'Object did not have an address')
    #       obj.save()
    #       messages.success(request, 'Object was moved to production!')
    
    
    
    
    
    #for each in queryset:
    #    (obj, created) = ExcavateAppExcavatemodel.objects.using('default2').get_or_create(id=127,excavate=each.excavate,bore=each.bore,applicant_name=each.applicant_name,company=each.company,reason_for_excavation_or_boring=each.reason_for_excavation_or_boring,location_of_excavation_including_termination_points=each.location_of_excavation_including_termination_points,start_date_for_excavation=each.start_date_for_excavation,projected_end_date_for_excavation=each.projected_end_date_for_excavation,reviewed_by=each.reviewed_by,meeting_held_with_applicant=each.meeting_held_with_applicant,date_of_approval=each.date_of_approval,server=each.server)
    #    if not obj.excavate or not obj.bore:
    #        messages.error(request, 'Form from %s : %s, has not chosen \'Excavate\' or \'Bore\'' % (obj.applicant_name, obj.company))
    #    elif obj.reviewed_by == None:
    #        messages.error(request, 'Form from %s : %s, has no data for \'Reviewed by\'' % (obj.applicant_name, obj.company))
    #    elif not obj.meeting_held_with_applicant:
    #        messages.error(request, 'Form from %s : %s, needs to have \'Meeting held with applicant\' checked' % (obj.applicant_name, obj.company))
    #    elif obj.date_of_approval == "":
    #        #You can also use warning, debug, info and success in place of error
    #        messages.error(request,'Form from %s : %s, has no data for \'Date of approval\'' % (obj.applicant_name, obj.company))
    #    else:
    #        queryset.update(server='prod')
    #        obj.save()
    #        messages.success(request, 'Request from %s : %s, has been copied to the production server' % (obj.applicant_name, obj.company))


class ExcavateAdmin(admin.ModelAdmin):
    search_fields = ['company'] #We can search by 'company'
    list_display = ('applicant_name','company','excavate_bore','server') #We will only see the following fields as columns in the admin page
    fieldsets = ( #How the 'excavatebore' object is displayed in the editor in the admin page
        ('Permit type', {
            'fields': ('excavate_bore',) 
        }),
        ('Application information', {
            'classes': ('collapse',), #Makes this header collapsible
            'fields': ('applicant_name','company') #These two fields will be under the parent header 'Application Information'
        }),
        ('Project information', {
            'classes': ('collapse',),
            'fields': ('reason_for_excavation_or_boring','location_of_excavation_including_termination_points','start_date_for_excavation','projected_end_date_for_excavation')
        }),
        ('Administrator action', {
            'fields': ('reviewed_by','meeting_held_with_applicant','date_of_approval','server')
        })
    )
    list_filter = ('server','excavate_bore','company') #A quick filter will have these fields available to search by
    readonly_fields = ('excavate_bore','server') #You will not be able to change these fields when editing an 'excavatebore' object
    actions = [push_to_production] #Includes the action we defined earlier in this page

#admin.site.register(ExcavateProxy)    #If making a proxy, you only have to register the proxy, not the model nor the admin
admin.site.register(ExcavateModel, ExcavateAdmin) #Always be sure to add the model before adding the admin class

