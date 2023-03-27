from django.shortcuts import render
from django.http import JsonResponse
from .chatbot_settings import get_response

def index(request):
    return render(request, 'index.html')

def receive_message(request):
    message = request.GET.get('message')
    response = get_response(message)
    return JsonResponse({'message': response})