from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json

# WIP - doesn't work

def chatbot_request(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input', '')
        print(f"Received user input: {user_input}")  # Debugging statement
        response = {
            'response': f'Hello, I have received your message, it reads: {user_input}'
        }
        return JsonResponse(response)
    else:
        return JsonResponse({'response': 'Invalid request method'})