from django.urls import path
from .views import last_10_events


urlpatterns = [
    path('', last_10_events)
]
