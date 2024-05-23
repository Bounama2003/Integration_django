from django import forms
from . models import Patient, Rendez_vous
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PatientForms(forms.ModelForm):
    class Meta:
        model=Patient
        fields='__all__'

class RendezvousForm(forms.ModelForm):
    class Meta:
        model=Rendez_vous
        fields='__all__'


class UserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'password1',
            'password2'
        ]

