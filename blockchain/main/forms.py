from django import forms
from django.http import request

class UserForm(forms.Form):
  username = forms.CharField()
  email = forms.EmailField()