from django.shortcuts import render
from .forms import Registrationform
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "main/index.html",)

def about(request):
    return render(request, 'main/about.html')

def reg(request):
    userform = Registrationform()
    return render(request, 'main/reg.html', {"form": userform} )

def login(request):
    return render(request, 'main/login.html')