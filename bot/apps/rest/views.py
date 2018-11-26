from rest_framework.views import APIView
from rest_framework.response import Response
import requests


class Last10EventsView(APIView):
    authentication_classes = []

    def post(self, request):
        events = requests.get(
            'https://test.bop.rest/api/feed/',
            headers={'Authorization': 'Token 233e7ef7888d82e098b3d63ca2a888d0e32a0eea'}).json()

        requests.get(
            'https://api.telegram.org/bot783030784:AAGA7zS4twvgcotcghkLPm-xPfrTn7h91SE/sendMessage',
            params={
                'chat_id': request.data['message']['chat']['id'],
                'text': ''.join('{time} {name}\n'.format(time=i['time'], name=i['name']) for i in events)}
        )

        return Response(status=204)
