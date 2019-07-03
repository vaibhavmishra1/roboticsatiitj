from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import IITJUser,Project,Feedback

class RegistrationForm(UserCreationForm):
    class Meta:
        model = IITJUser
        
        fields=["username","first_name","last_name","email","contact","hostel"]

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = Project
        fields="__all__"

class FeedbackCreateForm(forms.Form):
    description=forms.CharField(required=False)
    