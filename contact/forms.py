# forms.py
from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = contact
        fields = ['firstName', 'lastName', 'emailId','message']
