from django.contrib import admin
from django.urls import re_path
from user import api 
urlpatterns = [
    re_path('login', api.login, name='login'),
    re_path('', api.register, name='register'),
]