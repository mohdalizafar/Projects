from django import forms
from .models import Record
class Addrecords( forms.ModelForm):
    
    First_Name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    Last_Name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    Email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}), label="")
    City = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "City", "class": "form-control"}), label="")
    Phone = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Phone number", "class": "form-control"}), label="")

    class Meta:
        model=Record
        
        exclude= ("user", )
