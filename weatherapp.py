import requests
import json
import os
from win32com.client import Dispatch

speak = Dispatch("SAPI.SpVoice").Speak

def weather(querry):
    a = requests.get(f'http://api.weatherapi.com/v1/current.json?key=3c38dfe0d1bf445ea6874504232603&q={querry}')
    response = a.text

    json_data = json.loads(response)
    t = json_data['current']['temp_c']
    speak(f'The current temperature in {querry} is {t}degrees')


querry = input("Enter country name or city name here: ")
weather(querry)