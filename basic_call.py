import requests
import json
import urllib.request

url ="https://api.openweathermap.org/data/2.5/onecall?lat=10.075239&lon=108.224136&exclude=current,minutely,daily,alerts&appid=a68a0ee8420eb5ffcb2a5ce643107da7"

api_key = "Openweather key"
lat = "10.075239"
lon = "108.224136"
location = "Turan"
exclude = "current,minutely,daily"
# Get weather
url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={}&appid={}".format(lat,lon,exclude, api_key)
response = requests.get(url)
data = json.loads(response.text)
print(data)
print("Temperature is ", data["dt"][0]["main"]["temp"])
