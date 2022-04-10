from .models import DoctorVisit, FamilyVisit, MedicineList, Trips, Takeouts
from django import forms
from django.forms import ModelForm


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
        fields = ('location', 'Noofpeople', 'date', 'time', 'reason')


class DoctorVisitsForm(ModelForm):
    doctor = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Doctor",
                "class": "form-control"
            }
        ), required=False)
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


class MedicineForm(ModelForm):
    medicine = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Medicine",
                "class": "form-control"
            }
        ))
    Nooftimesaday = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "No of times a day",
                "class": "form-control"
            }
        ),
        required=False)
    fromdate = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "From",
                "class": "form-control"
            }
        ),
        required=False)
    to = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "To",
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
        model = MedicineList
        fields = ('medicine', 'Nooftimesaday', 'fromdate', 'to', 'reason')


class TripsForm(ModelForm):
    destination = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Destination",
                "class": "form-control"
            }
        ), required=False)
    duration = forms.IntegerField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Duration",
                "class": "form-control"
            }
        ),
        required=False)
    fromdes = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "From",
                "class": "form-control"
            }
        ),
        required=False)
    to = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "To",
                "class": "form-control"
            }
        ),
        required=False)

    class Meta:
        model = Trips
        fields = ('destination', 'duration', 'fromdes', 'to')


class TakeoutsForm(ModelForm):
    restaurant = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Restaurant / Cafe",
                "class": "form-control"
            }
        ), required=False)
    type = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Type",
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
    time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "placeholder": "To",
                "class": "form-control"
            }
        ),
        required=False)

    class Meta:
        model = Takeouts
        fields = ('restaurant', 'type', 'date', 'time')
