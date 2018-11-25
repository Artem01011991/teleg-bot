from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from braces.views import CsrfExemptMixin
import requests


class Last10EventsView(CsrfExemptMixin, APIView):
    authentication_classes = []

    @csrf_exempt
    def post(self, request):
        if request.method == 'POST':
            requests.get(
                'https://api.telegram.org/bot783030784:AAGA7zS4twvgcotcghkLPm-xPfrTn7h91SE/sendMessage',
                params={'chat_id': request.POST['message']['chat']['id'], 'text': 'Hello'}
            )

        return Response(status=204)
