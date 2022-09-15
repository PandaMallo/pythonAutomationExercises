#openweathermap.or
from urllib import response
import requests

baseUrl = 'http://api.openweathermap.org/data/2.5/forecast'
parameters = {'APPID' : 'YOUR_KEY', 'q' : 'Seattle, US'}
response = requests.get(baseUrl, params= parameters)
#Verify connection is stablish
print(response.content)