from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class Last10EventsView(APIView):
    authentication_classes = []

    def post(self, request):
        requests.get(
            'https://api.telegram.org/bot783030784:AAGA7zS4twvgcotcghkLPm-xPfrTn7h91SE/sendMessage',
            params={'chat_id': request.data['message']['chat']['id'], 'text': 'Hello'}
        )

        return Response(status=204)
