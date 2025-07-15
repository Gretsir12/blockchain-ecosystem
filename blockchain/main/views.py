from django.shortcuts import render, redirect
from .forms import Registrationform, LoginForm, Verify_codeForm
from .scripts import *

# Create your views here.

def index(request):
    return render(request, "main/index.html",)


def about(request):
    return render(request, 'main/about.html')


def reg(request):
    if request.method == "POST":
        userform = Registrationform(request.POST)
        if userform.is_valid():
            # Access cleaned data with userform.cleaned_data
            username = userform.cleaned_data['username']
            email = userform.cleaned_data['email']
            password = userform.cleaned_data['password']
            DEBUG(username, email, password)            
            Send_mail(email)
            return redirect('/verify_code')
        else:
            return render(request, 'main/reg.html', {"form": userform})
    else:
        userform = Registrationform()

    return render(request, 'main/reg.html', {"form": userform} )


def login(request):
    if request.method == "POST":
        userform = LoginForm(request.POST)
        if userform.is_valid():
            # Access cleaned data with userform.cleaned_data
            email = userform.cleaned_data['email']
            password = userform.cleaned_data['password']
            DEBUG(email, password, username=None)
            return redirect('/verify_code')
        else:
            return render(request, 'main/login.html', {"form": userform})
    else:
        userform = LoginForm()
        return render(request, 'main/login.html', {"form": userform})


def Verify_code(request):
    userform = Verify_codeForm()
    if request.method == "POST":
        code = request.POST.get('code')
        if code == '123456':  # Example verification logic
            return redirect('/success')
        else:
            return render(request, 'main/verify_code.html', {"error": "Invalid code"})
    return render(request, 'main/verify_code.html', {"form": userform})