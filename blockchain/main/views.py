from django.shortcuts import render, redirect
from .forms import Registrationform, LoginForm
from .scripts import DEBUG, Send_mail

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
            passwd = userform.cleaned_data['passwd']
            DEBUG(username, email)
            return redirect('/login')
        else:
            # Form is not valid, errors will be shown in the template
            return render(request, 'main/reg.html', {"form": userform})
    else:
        userform = Registrationform()

    return render(request, 'main/reg.html', {"form": userform} )


def login(request):
    userform = LoginForm()
    return render(request, 'main/login.html', {"form": userform})