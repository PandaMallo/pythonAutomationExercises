#https://wwww.selenium.dev
#locate elem by id 'q' and print 
#locate elem by name 'q' and print 
#locate elem by heading 'Getting Started' by Xpath and print 
#locate elem by class 'selenium-sponsors' and print 

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://wwww.selenium.dev')

htmlElem = driver.find_element_by_id('q')
print(htmlElem)


htmlElemName = driver.find_element_by_name('q')
print(htmlElemName)


htmlElemXpath = driver.find_element_by_xpath('/html/body/div/main/div[2]/h2')
print(htmlElemXpath)


classNameElem = driver.find_element_by_class_name('selenium-sponsors')
print(classNameElem)


driver.close()