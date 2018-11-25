from django.http import HttpResponse
import requests


def last_ten_events_view(request):
    if request.POST['message']['text'] == '/feed':
        requests.get(
            'https://api.telegram.org/bot783030784:AAGA7zS4twvgcotcghkLPm-xPfrTn7h91SE/sendMessage',
            params={'chat_id': request.POST['message']['chat']['id'], 'text': 'Hello'}
        )

    return HttpResponse(status=204)
