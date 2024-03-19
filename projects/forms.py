from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import PasswordInput, TextInput
from .models import Project



class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'location', 'company','manager']




class UpdateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'location', 'company','manager']