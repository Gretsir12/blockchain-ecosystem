from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index), #main page
    path('about', views.about), #page about us
    path('reg', views.reg), # registration page
    path('login', views.login), # login page
    path('verify_code', views.Verify_code), # verification code page
]
