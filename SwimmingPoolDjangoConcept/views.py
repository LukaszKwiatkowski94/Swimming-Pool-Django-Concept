from urllib import request
from django.shortcuts import render

def home(request):
    context = {

    }
    return render(request, 'home.html',context)

def page403(request):
    context = {

    }
    return render(request, 'error.html',context)