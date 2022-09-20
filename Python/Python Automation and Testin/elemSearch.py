from selenium import webdriver

driver = webdriver.Chrome()

#Elements by ID atribute
driver.get('https://www........com')
htmlElem = driver.find_element_by_id('html_id')
print('My html element is:')
print(htmlElem)
driver.close()

#Searchin elements by name
driver.get('https://www........com')
htmlElemName = driver.find_element_by_name('html_name')
print('My html element is:')
print(htmlElemName)
driver.close()

#Search element by Xpath
#Absolut
driver.get('https://www........com')
htmlElemXpath = driver.find_element_by_xpath('/html/body/elem')
print('My html element is:')
print(htmlElemXpath)
driver.close()
#Relative
driver.get('https://www........com')
htmlElemXpath = driver.find_element_by_xpath('//elem')
htmlElemXpathSpecific = driver.find_element_by_xpath("//@id='html_id'")
print('My html xpath element is:')
print(htmlElemXpath)
print('My html xpath with id element is:')
print(htmlElemXpathSpecific)
driver.close()

#Search element by Class
driver.get('https://www........com')
classElem = driver.find_element_by_class_name('html_class_name')
print('My class element is:')
print(classElem)
driver.close()