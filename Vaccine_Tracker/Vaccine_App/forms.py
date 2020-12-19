from django import forms

class LocationForm(forms.Form):
    loc = forms.CharField(label='Please enter your address')
