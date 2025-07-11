from django import forms

class Registrationform(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    email = forms.EmailField()
    passwd = forms.CharField(widget=forms.PasswordInput)


class Verify_codeForm(forms.Form):
    code = forms.CharField(label='Код подтверждения', max_length=6, min_length=6, required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Введите код подтверждения'}))