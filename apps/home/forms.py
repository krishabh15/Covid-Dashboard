from django import forms
from django.forms import ModelForm
from .models import DoctorVisit


class DoctorVisitsForm(ModelForm):
    doctor = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Doctor",
                "class": "form-control"
            }
        ))
    visit_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Visit Date",
                "class": "form-control"
            }
        ),
        required=False)
    reason = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Reason for Visit",
                "class": "form-control"
            }
        ),
        required=False)
    notes = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Notes",
                "class": "form-control"
            }
        ),
        required=False)

    class Meta:
        model = DoctorVisit
        fields = ('doctor', 'visit_date', 'reason', 'notes')
