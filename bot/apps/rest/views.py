from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests


@api_view
def last_10_events(request):
    if request.method == 'POST':
        requests.get(
            'https://api.telegram.org/bot783030784:AAGA7zS4twvgcotcghkLPm-xPfrTn7h91SE/sendMessage',
            params={'chat_id': request.POST['message']['chat']['id'], 'text': 'Hello'}
        )

    return Response(status=204)
