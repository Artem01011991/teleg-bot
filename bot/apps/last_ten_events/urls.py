from django.urls import path
from .views import last_ten_events_view


urlpatterns = [
    path('last-ten-events', last_ten_events_view)
]
