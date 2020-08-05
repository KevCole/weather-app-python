import requests
import json
import math
import config

#################################### Get Latitude and Longitude with IPSTACK API ###############################################

response = requests.get("http://api.ipstack.com/check?access_key=" + config.access_key)

json_response = response.json()



long = str(json_response["longitude"])
lat = str(json_response["latitude"])

################################################################################################################################



weather_response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=" + lat + "&lon=" + long + "&units=imperial&exclude=hourly,daily&appid=" + config.key)
json_weather_response = weather_response.json()

whats_the_weather = round(json_weather_response["current"]["temp"])
feels_like = round(json_weather_response["current"]["feels_like"])
print(f"Currently the weather is {whats_the_weather}")
print(f"The real feel is {feels_like} degrees")





