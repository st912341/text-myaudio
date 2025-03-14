from django.urls import path
from .views import text_to_speech

urlpatterns = [
    path('index/', text_to_speech, name='indexp/'),
]
