import pyttsx3
from django.shortcuts import render
from django.http import FileResponse
import os

def text_to_speech(request): 
    return render(request, "tts_app/index.html")
