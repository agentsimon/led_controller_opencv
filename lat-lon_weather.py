import requests
import json
import datetime

#Get latitude and longitude of nearest city from Air Visual
url = "http://api.airvisual.com/v2/nearest_city?key={Your Air Visual key}"
response = requests.request('GET', url)
raw_data = json.loads(response.text)
measurements = []
print(raw_data)
lon = raw_data["data"]["location"]["coordinates"][0]
lat = raw_data["data"]["location"]["coordinates"][1]
print("Latitude is ", lat, "Longitude is ", lon)
# Get weather from OpenWeather
exclude = "current,minutely,daily"
api_key = "Your OpenWeather key"
url = "https://api.openweathermap.org/data/2.5/onecall?lat={}&lon={}&exclude={}&appid={}".format(lat,lon,exclude, api_key)
response = requests.get(url)
data = json.loads(response.text)
#Print the forecast 
date_info = data["hourly"][2]["dt"]
print("Date is", datetime.datetime.fromtimestamp(date_info).strftime('%Y-%m-%d %H:%M:%S'), "Temperature will be", data["hourly"][2]["temp"], "Kelvin")
