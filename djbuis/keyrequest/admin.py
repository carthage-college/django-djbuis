#admin.py is where we create 'actions' that users can do to entries
#within this app, excavatebore, as well as settings to change how
#we view entries within 'excavatebore'

#'admin' - necessary to change view settings when viewing an 'excavatebore' object
from django.contrib import admin
from djbuis.keyrequest.models import Keys
from django.contrib.admin.models import LogEntry, DELETION
from django.utils.html import escape
from django.core.urlresolvers import reverse

#This is the code that makes a log of all changes in the database. Dont touch it.
class LogEntryAdmin(admin.ModelAdmin):

    date_hierarchy = 'action_time'

    readonly_fields = LogEntry._meta.get_all_field_names()

    list_filter = [
        'user',
        'content_type',
        'action_flag'
    ]

    search_fields = [
        'object_repr',
        'change_message'
    ]


    list_display = [
        'action_time',
        'user',
        'content_type',
        'object_link',
        'action_flag',
        'change_message',
    ]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser and request.method != 'POST'

    def has_delete_permission(self, request, obj=None):
        return False

    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = u'<a href="%s">%s</a>' % (
                reverse('admin:%s_%s_change' % (ct.app_label, ct.model), args=[obj.object_id]),
                escape(obj.object_repr),
            )
        return link
    object_link.allow_tags = True
    object_link.admin_order_field = 'object_repr'
    object_link.short_description = u'object'

#This is an 'action' a user can perform to a 'keyrequest' object
def push_to_database(modeladmin, request, queryset):
	#for item in queryset:
	#	FinprivRec.objects.using('productiondefault').get_or_create(id=item.Carthage_ID_Number, code_name=item.name)
		
    push_to_database.short_description = "Approve for moving to another database"

class Admin(admin.ModelAdmin):
	list_display = ('issued_to', 'building') #We will only see the following fields as columns in the admin page
	actions = [push_to_database]  #Includes the action we defined earlier in this page
	
admin.site.register(Keys, Admin) #Always be sure to add the model before adding the admin class
admin.site.register(LogEntry, LogEntryAdmin) #Only one model and an admin class can be associated with a call to register. If you have more models, make more calls.
