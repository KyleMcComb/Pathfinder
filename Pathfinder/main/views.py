from django.shortcuts import render
from django.http import JsonResponse
from .chatbot_settings import get_response
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

def verify(request):
    #username = request.POST["username"]
    #password = request.POST["password"]
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({'loggedIn': 'true'})
    else:
        return JsonResponse({'loggedIn': 'false'})

def index(request):
    return render(request, 'index.html')

def receive_message(request):
    message = request.GET.get('message')
    response = get_response(message)
    return JsonResponse({'message': response})

def settings(request):
    return render(request, 'settings.html')

def gradeDashboard(request):
    return render(request, 'gradeDashboard.html')

def moduleInformation(request):
    return render(request, 'moduleInformation.html')
