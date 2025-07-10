from django import forms
from django.http import request

class Registrationform(forms.Form):
  email = forms.EmailField()
  username = forms.CharField()
  passwd = forms.PasswordInput()

class LoginForm(forms.Form):
  email = forms.EmailField()
  passwd = forms.PasswordInput()