print ('Welcome. Please enter your zip code or city.')
zipCity = input ('In the field below, please type your City or Zip Code:')
#this is the request field

$ pip install requests-2.24.0.tar.gz
#python is installing the requests library

response = requests.get('http://google.com')
enter(zipCity)
if response !== "Search instead for...":
	response = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={0d10eedd637db9ce12d3b7ecc52964d8}')
#this is where python is accessing the api
		if response == 200
  			response.put (zipCity)
  		else:
  			print(f"(There was an issue accessing the website. Please wait a few minutes and try again")
  			response = requests.get('http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={0d10eedd637db9ce12d3b7ecc52964d8}')
  #this is checking to make sure the api wwas able to be pulled succesfully
 else:
 	print(This is not a valid city and/or zip code. Please try again.)

weatherPattern = x
  #at this point, the website should have displayed what the weather pattern is
print("The weather for, 'zipCity' is 'weatherPattern.' ")
#the final step is the weather forecast being displayed for the User.