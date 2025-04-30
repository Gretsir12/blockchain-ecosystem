from . import views
from django.urls import path

urlpatterns = [
  path('auth', views.auth)
]