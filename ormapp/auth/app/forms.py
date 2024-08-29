from django import forms
from .models import Record
class customform(forms.ModelForm ):
    name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    position = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter your position'}))
    number = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'}))

    class Meta:
        model=Record
        fields = ['name', 'position', 'number']