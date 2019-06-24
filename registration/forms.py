from django import forms

from .models import IITJUser

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = IITJUser
        fields = ['username','password','first_name','last_name','email','contact','hostel']