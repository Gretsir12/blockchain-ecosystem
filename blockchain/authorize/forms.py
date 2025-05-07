from django import forms

# class form(forms.Form):
#     email = forms.CharField(label="Your email:")

class UserForm(forms.Form):
    name = forms.CharField(label="Enter your name:")
    age = forms.IntegerField(label="Enter your age:")