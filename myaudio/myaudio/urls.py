from django.urls import path
from .views import text_to_speech

urlpatterns = [
    path('text_to_speech/', text_to_speech, name='text_to_speech'),  # Removed the trailing slash from the name
]
