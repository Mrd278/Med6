from django.contrib.auth.forms import UserCreationForm
from .models import patient
from django import forms
from django.forms import ModelForm

class ProfileForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = ('patient_name','gender','age','ph_no','patient_address','pat_email_id')

class Booking_form(forms.ModelForm):
    class Meta:
        model=patient
        fields=('patient_name','ph_no')