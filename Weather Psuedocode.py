import json
import requests
#python is installing the requests library
def this_api():
    """welcome user and explain"""
    print("Welcome to my attempt at an API. Below you will be prompted for your City or Zip code to get the data from OpenWeatherMap.org.")
    
this_api()
#function
while True:
    zipCity = input ('In the field below, please type your City or Zip Code:')
#this is the request field

api_key = "0d10eedd637db9ce12d3b7ecc52964d8"

city = ('zipCity')
url = "https://api.openweathermap.org/data/2.5/onecall?city=%s&appid=%s&units=imperial"% (city, api_key)

response=requests.get(url)
data = json.loads(response.text)
current = data["current"]["dt"]
if response = '200'
    print(current)
    else:
        print(f"(There was an issue accessing the website. Please wait a few minutes and try again.")
 #this is checking to make sure the api was able to be pulled succesfully

print("The weather for, 'zipCity' is 'current.' ")
#the final step is the weather forecast being displayed for the User.
