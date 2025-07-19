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
            username = userform.cleaned_data['username']
            email = userform.cleaned_data['email']
            password = userform.cleaned_data['password']
            DEBUG(username, email, password)
            
            from .models import User
            #sending verification email
            User.objects.create(username=username, email=email)
            send_verification_email(User)
            
            # Redirect to verification code page
            # Assuming you have a view for verifying the code
            # You can also store the user in session or database if needed
            print(f'DEBUG: User {username} code succsessfully sent')

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
    if request.method == "POST":
        code = request.POST.get('code')
        if code == '123456':  # Example verification code, replace code generator in future
            return redirect('/success')
        else:
            return render(request, 'main/verify_code.html', {"error": "Invalid code"})
    else:
        userform = Verify_codeForm()
        return render(request, 'main/verify_code.html', {"form": userform})
