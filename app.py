import requests
import json
access_key = "21dc354c69fd878156565f73dc03638f"
response = requests.get("http://api.ipstack.com/check?access_key=" + access_key)
json_response = response.json()
secret_key = "1a765ec287af0c5b80d9b6a186eb3ee0"



#http://api.ipstack.com/check? access_key = {location_secret_key}
#response = requests.get("https://api.openweathermap.org/data/2.5/onecall?lat=33.441792&lon=-94.037689&exclude=hourly,daily&appid={key}")



print(json_response["latitude"])
print(json_response["longitude"])

