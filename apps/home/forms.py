from django import forms
from django.forms import ModelForm
from .models import DoctorVisits


class DoctorVisitsForm(ModelForm):
	class Meta:
		model = DoctorVisits
		fields = ('doctor', 'visit_date', 'reason', 'notes')

		labels = {
			'doctor_name': '',
			'visit_date': 'YYYY-MM-DD',
			'reason': 'Reason',
			'notes': 'Notes',	
		}
		widgets = {
            'doctor': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Doctor Name'}),
            'visit_date': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Visit Date'}),
            'reason': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Reason'}),
            'notes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Notes'}),
		}