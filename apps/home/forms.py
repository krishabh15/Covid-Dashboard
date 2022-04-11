from .models import DoctorVisit, FamilyVisit, MedicineList, Trips, Takeouts
from django import forms
from django.forms import ModelForm


class FamilyVisitsForm(ModelForm):
    location = forms.CharField(
        widget=forms.TextInput(
            attrs={

                "class": "form-control"
            }
        ))
    Noofpeople = forms.CharField(
        widget=forms.TextInput(
            attrs={

                "class": "form-control"
            }
        ),
        required=False)
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control"
            }
        ),
        required=False)
    time = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "time",
                "class": "form-control"
            }
        ),
        required=False)
    reason = forms.CharField(
        widget=forms.TextInput(
            attrs={

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

                "class": "form-control"
            }
        ), required=False)
    visit_date = forms.DateField(
        widget=forms.DateInput(
            attrs={

                "class": "form-control",
                "type": "date",
            }
        ),
        required=False)
    reason = forms.CharField(
        widget=forms.TextInput(
            attrs={

                "class": "form-control"
            }
        ),
        required=False)
    notes = forms.CharField(
        widget=forms.TextInput(
            attrs={

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

                "class": "form-control"
            }
        ))
    Nooftimesaday = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "class": "form-control",

            }
        ),
        required=False)
    fromdate = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "date",
                "class": "form-control"
            }
        ),
        required=False)
    to = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "type": "date",
                "class": "form-control"
            }
        ),
        required=False)
    reason = forms.CharField(
        widget=forms.TextInput(
            attrs={

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

                "class": "form-control"
            }
        ), required=False)
    duration = forms.IntegerField(
        widget=forms.TextInput(
            attrs={

                "class": "form-control"
            }
        ),
        required=False)
    fromdes = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control"
            }
        ),
        required=False)
    to = forms.CharField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
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

                "class": "form-control"
            }
        ), required=False)
    type = forms.CharField(
        widget=forms.TextInput(
            attrs={

                "class": "form-control"
            }
        ),
        required=False)
    date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "type": "date",
                "class": "form-control"
            }
        ),
        required=False)
    time = forms.TimeField(
        widget=forms.TimeInput(
            attrs={
                "type": "time",
                "class": "form-control"
            }
        ),
        required=False)

    class Meta:
        model = Takeouts
        fields = ('restaurant', 'type', 'date', 'time')
