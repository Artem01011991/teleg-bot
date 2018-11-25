from django.urls import path
from .views import Last10EventsView


urlpatterns = [
    path('', Last10EventsView.as_view())
]
