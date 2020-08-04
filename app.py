import requests
import json

secret_key = "1a765ec287af0c5b80d9b6a186eb3ee0"

location_secret_key = "21dc354c69fd878156565f73dc03638f"

#http://api.ipstack.com/check? access_key = {location_secret_key}

#response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&exclude=hourly,daily&appid={key}")

response = requests.get("http://api.ipstack.com/check?access_key={location_secret_key} ")

print(response.status_code)