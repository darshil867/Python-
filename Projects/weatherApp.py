import os

import requests
import json


api_key = "dcb0a5fff4eb54708bb675787054dfd3"


city = input("Enter the name of the city: \n")


url = f"http://api.weatherstack.com/current?access_key=dcb0a5fff4eb54708bb675787054dfd3&query={city}"
r = requests.get(url)

wdic = json.loads(r.text)


w = wdic["current"]["temperature"]
print(f"The current temperature in {city} is {w}°C.")


os.system(f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'The current wheather in {city} is {w} degrees\')"')

# import requests
#
# url = "https://api.weatherstack.com/current?access_key=dcb0a5fff4eb54708bb675787054dfd3"
#
# querystring = {"query":"New Delhi"}
#
# response = requests.get(url, params=querystring)
#
# print(response.json())