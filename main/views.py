from database.models import *
from mysite.settings import *
from .forms import CustomLoginForm
from django.shortcuts import render
from django.http import JsonResponse
from .chatbot_settings import get_response

'''
    @Author: @KyleMcComb
'''
def receive_message(request):
    message = request.GET.get('message')
    response = get_response(message)
    return JsonResponse({'message': response})

'''
    @Author: @KyleMcComb
    @Description: Renders the index.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def index(request):
    return render(request, 'index.html', {'form': CustomLoginForm()})

'''
    @Author: @DeanLogan
    @Description: Renders the settings.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def settings(request):
    return render(request, 'settings.html', {'form': CustomLoginForm()})

'''
    @Author: @DeanLogan
    @Description: Renders the gradeDashboard.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def gradeDashboard(request):
    return render(request, 'gradeDashboard.html', {'form': CustomLoginForm()})

'''
    @Author: @DeanLogan
    @Description: Renders the moduleInformation.html file to be displayed to the user.
    @param: request -  HttpRequest object that contains metadata about the request
'''
def moduleInformation(request):
    return render(request, 'moduleInformation.html', {'form': CustomLoginForm()})
