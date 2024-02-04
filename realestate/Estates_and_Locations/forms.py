from django import forms
from .models import Estate 
from Clients_and_Contacts.models import Client


class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = '__all__'
        photo=forms.ImageField(widget=forms.FileInput())

class Sign(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['username', 'email', 'national_code', 'password']

        

