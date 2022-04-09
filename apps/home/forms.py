from django import forms
from django.forms import ModelForm
from .models import DoctorVisit


class DoctorVisitsForm(ModelForm):
    class Meta:
        model = DoctorVisit
        fields = ('doctor', 'visit_date', 'reason', 'notes')

        labels = {
            'doctor_name': '',
            'visit_date': 'YYYY-MM-DD',
            'reason': 'Reason',
            'notes': 'Notes',
        }
        widgets = {
            'doctor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doctor Name'}),
            'visit_date': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Visit Date'}),
            'reason': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Reason'}),
            'notes': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Notes'}),
        }
