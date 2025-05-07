from django.shortcuts import render
from .forms import form
from .forms import UserForm

# def auth(request):
#     email = form()
#     return render(request, "authorize/auth.html",
#                         {"form" : email})
    
def auth(request):
    userform = UserForm()
    return render(request, "authorize/auth.html",
                                 {"form" : userform})