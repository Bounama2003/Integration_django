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
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'heure': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'patient': forms.Select(attrs={'class': 'form-control'}),
        }


"""class UserForm(UserCreationForm):
    
    class Meta:
        model=User
        fields=[
            'username',
            'last_name',
            'email',
            'password1',
            'password2'
        ]
    from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User"""

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'email', 'password1', 'password2']

    widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
