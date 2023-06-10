import requests
import json
import win32com.client as wincom
speak=wincom.Dispatch("SAPI.SpVoice")
city=input("Enter the name of the city: ").capitalize()
url=f"http://api.weatherapi.com/v1/current.json?key=35c10bada3ec41ca81a52300231204&q={city}&api=no"


r=requests.get(url)
#print(r.text)
wdict= json.loads(r.text)
w=wdict["current"]["temp_c"]
speak.Speak(f"Weather of {city} is{w}")



