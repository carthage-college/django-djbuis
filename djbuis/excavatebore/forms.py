from django import forms
from djbuis.excavatebore.models import ExcavateModel
from django.contrib.admin import widgets

class ExcavateForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(ExcavateForm, self).__init__(*args,**kwargs)
		
		self.fields['start_date_for_excavation'].error_messages = {'required': 'Use this format:mm/dd/yyyy','invalid': 'Try this format:mm/dd/yyyy'}
		self.fields['projected_end_date_for_excavation'].error_messages = {'required': 'Use this format:mm/dd/yyyy','invalid': 'Try this format:mm/dd/yyyy'}
		
	def clean(self):
		cleaned_data = super(ExcavateForm, self).clean()
		
		excavate = cleaned_data.get("excavate")
		bore = cleaned_data.get("bore")
		
		if excavate == False and bore == False:

			msg = u"Please select either 'Excavate' or 'Bore'"
			self._errors["excavate"] = self.error_class([msg])
			self._errors["bore"] = self.error_class([msg])
			
			del cleaned_data["excavate"]
			del cleaned_data["bore"]
			
			
		return cleaned_data
		
	class Meta:
		model = ExcavateModel
		exclude = ['reviewed_by','meeting_held_with_applicant','date_of_approval','server']
		widgets = {
			'start_date_for_excavation' : forms.DateInput(attrs={'type':'date'}),
			'projected_end_date_for_excavation' : forms.DateInput(attrs={'type':'date'}),
		}
