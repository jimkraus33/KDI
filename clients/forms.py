from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Client



class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'location','email', 'phone', 'contacts']




class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'location','email', 'phone', 'contacts']