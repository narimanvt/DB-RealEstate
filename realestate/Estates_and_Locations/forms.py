from django import forms
from .models import Estate

class EstateForm(forms.ModelForm):
    class Meta:
        model = Estate
        fields = '__all__'
        photo=forms.ImageField(widget=forms.FileInput())
        

