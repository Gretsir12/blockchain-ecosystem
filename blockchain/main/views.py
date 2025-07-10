from django.shortcuts import render
from .forms import Registrationform
# from django.http import HttpResponse

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
            # ... process or save user data ...
            # Redirect or render a success page
        else:
            # Form is not valid, errors will be shown in the template
            return render(request, 'main/reg.html', {"form": userform})
    else:
        userform = Registrationform()
    return render(request, 'main/reg.html', {"form": userform} )

def login(request):
    return render(request, 'main/login.html')