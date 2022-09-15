import requests
from bs4 import BeautifulSoup

#One page scrape
url = 'http://scrapingclub.com/exercise/list_basic/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
counter = 1
for i in items:
    itemName = i.find('h4', class_ ='card-title').text.strip('\n') #the las part takes away the empty line between lines
    itemPrice = i.find('h5').text
    print('%s) Price: %s, Item Name: %s' % (counter, itemPrice, itemName))
    counter += 1

#Multipage scrape
pages = soup.find('ul', class_='pagination')
urls = []
links = pages.find_all('a', class_= 'page-link')
for link in links:
    pageNum = int(link.text) if link.text.isdigit() else None
    if pageNum != None:
        x = link.get('href')
        urls.append(x)
##Test if urls array print out
#print(urls)

counter = 1
for i in urls:
    newUrl = url + 1
    response = response.get(newUrl)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
    for i in items:
        itemName = i.find('h4', class_ ='card-title').text.strip('\n') #the las part takes away the empty line between lines
        itemPrice = i.find('h5').text
        print('%s) Price: %s, Item Name: %s' % (counter, itemPrice, itemName))
        counter += 1
