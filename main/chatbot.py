from django.http import JsonResponse

def receive_message(request):
    user_input = request.GET.get('message', '')
    response_data = {
        'message': f"I have received your message, you entered: {user_input}"
    }
    return JsonResponse(response_data) 

#may not be needed anymore - keeping it just incase atm until chatterbot is fully set up