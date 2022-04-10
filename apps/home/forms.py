from django import forms
from django.forms import ModelForm
from .models import DoctorVisit
from .models import FamilyVisit


class FamilyVisitsForm(ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Location",
                "class": "form-control"
            }
        ))
    Noofpeople = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "No of people",
                "class": "form-control"
            }
        ),
        required=False)
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Date",
                "class": "form-control"
            }
        ),
        required=False)
    time = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Time",
                "class": "form-control"
            }
        ),
        required=False)
    reason = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Reason",
                "class": "form-control"
            }
        ),
        required=False)

    class Meta:
        model = FamilyVisit
        fields = ('location', 'Noofpeople', 'date', 'time' , 'reason')

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
