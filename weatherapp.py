import requests
import json
import os
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak

def weather(querry):
    a = requests.get(f'api_here')
    response = a.text

    json_data = json.loads(response)
    t = json_data['current']['temp_c']
    speak(f'The current temperature in {querry} is {t}degrees')


querry = input("Enter country name or city name here: ")
weather(querry)