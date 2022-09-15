import requests
import json

baseUrl ='https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc' : '0012993441012' }
response = requests.get(baseUrl, params=parameters)
#testing. The result must be an exact match of the complete url
print(response.url)

content = response.content
info = json.loads(content)
##Verify info type(should be a dictionary) and Print all the info in the console
#print(type(info))
#print(info)

item = info['items']
itemInfo = item[0]
title = itemInfo['title']
brand = itemInfo['brand']
#Check info is correct
print(title)
print(brand)