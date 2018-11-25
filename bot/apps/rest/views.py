from rest_framework.views import APIView
from rest_framework.response import Response
from .auth_classes import CsrfExemptSessionAuthentication
import requests


class Last10EventsView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request):
        if request.method == 'POST':
            requests.get(
                'https://api.telegram.org/bot783030784:AAGA7zS4twvgcotcghkLPm-xPfrTn7h91SE/sendMessage',
                params={'chat_id': request.POST['message']['chat']['id'], 'text': 'Hello'}
            )

        return Response(status=204)
