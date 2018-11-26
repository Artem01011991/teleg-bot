from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import datetime


class Last10EventsView(APIView):
    authentication_classes = []

    def post(self, request):
        if request.data['message']['text'] == '/feed':
            # events = requests.get(
            #     'https://test.bop.rest/api/feed/',
            #     headers={'Authorization': 'Token 233e7ef7888d82e098b3d63ca2a888d0e32a0eea'}).json()[-10:]

            events = [
                {'id': 65590, 'time': '2017-07-31T13:35:00Z', 'name': 'Dutra Silva R./Lorenzi P. - Podlipnik-Castillo H./Vasilevski A.'},
                {'id': 61468, 'time': '2017-08-05T21:00:00Z', 'name': 'Atletico Veraguense - Tauro'},
                {'id': 67769, 'time': '2017-08-07T11:50:00Z', 'name': 'Shofayziyev S./Tsivadze G. - Canter А./Moreno De Alboran N.'},
                {'id': 68764, 'time': '2017-08-08T10:30:00Z', 'name': 'Udvardy P. - Dascalu N.-C.'},
                {'id': 68615, 'time': '2017-08-08T15:00:00Z', 'name': 'Murray S. - Kolar N.'},
                {'id': 67768, 'time': '2017-08-09T09:40:00Z', 'name': 'Stephens Sl. - Hoang A.'},
                {'id': 70429, 'time': '2017-08-12T14:10:00Z', 'name': 'Pavic A. - Escobedo E.'},
                {'id': 70445, 'time': '2017-08-12T16:06:00Z', 'name': 'Barthel M. - Diyas Z.'},
                {'id': 70446, 'time': '2017-08-12T17:35:00Z', 'name': 'Albot R. - Youzhny M.'},
                {'id': 69445, 'time': '2017-08-13T12:30:00Z', 'name': 'Hungary - Germany'}]


            requests.get(
                'https://api.telegram.org/bot783030784:AAGA7zS4twvgcotcghkLPm-xPfrTn7h91SE/sendMessage',
                params={
                    'chat_id': request.data['message']['chat']['id'],
                    'text': ''.join('{time} {name}\n'.format(
                        time=datetime.datetime.strptime(i['time'], "%Y-%m-%dT%H:%M:%SZ").__str__(),
                        name=i['name']
                    ) for i in events)}
            )

        return Response(status=204)
