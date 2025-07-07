from django.shortcuts import render
from .forms import UserForm
# from django.http import HttpResponse

# Create your views here.

def index(request):
    userform = UserForm()
    return render(request, "main/index.html",
    { "form": userform })

def about(request):
    return render(request, 'main/about.html')

def reg(request):
    return render(request, 'main/reg.html')

def login(request):
    return render(request, 'main/login.html')
