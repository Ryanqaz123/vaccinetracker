from django import forms

class LocationForm(forms.Form):
    loc = forms.CharField(label='Please enter your address')

class CenterForm(forms.Form):
    name = forms.CharField(label='What is the name of your vaccination center?')
    # password = forms.Char
    address= forms.CharField(label='What is the address of your vaccination center?')
    email = forms.EmailField(label='What is your email?')
    phone = forms.CharField(label='What is your phone number?')
    description = forms.CharField(label='Write a brief description regarding your vaccination center', widget=forms.Textarea)
    pfp = forms.ImageField(label='Upload a Profile Picture')
