from django import forms
from .models import Record
class Addrecords( forms.ModelForm):
    # we don't need created at here as django already does for us
    First_Name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "First Name", "class": "form-control"}), label="")
    Last_Name = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Last Name", "class": "form-control"}), label="")
    Email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={"placeholder": "Email", "class": "form-control"}), label="")
    City = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "City", "class": "form-control"}), label="")
    Phone = forms.CharField(required=True, widget=forms.TextInput(attrs={"placeholder": "Phone number", "class": "form-control"}), label="")

    class Meta:
        model=Record
        #fields = ["First_Name", "Last_Name", "Email", "City", "Phone"]
        exclude= ("user", )
