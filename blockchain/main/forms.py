from django import forms

class emailform(forms.Form):
    usermail = forms.Charfield(label="Your email:")