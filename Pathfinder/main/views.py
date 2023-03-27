from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html')

def settings(request):
    return render(request, 'settings.html')

def gradeDashboard(request):
    return render(request, 'gradeDashboard.html')

def moduleInformation(request):
    return render(request, 'moduleInformation.html')