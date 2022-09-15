import requests
from bs4 import BeautifulSoup


#Take HTML tree from source
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
##Test connection
#print(soup)

quotes = soup.find_all('span', class_='text')
##Test all quotes show up in the terminal
#print(quotes)
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='tags')

for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    #Identify the general section where multiple tagas are and then iterate throug them to find the specifics tags of each quote
    quoteTags = tags[i].find_all('a', class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)