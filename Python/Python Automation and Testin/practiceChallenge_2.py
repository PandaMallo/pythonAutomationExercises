#https://wwww.selenium.dev
#locate elem by id 'gsc-iw-id1' and print 
#locate elem by name 'submit' and print 
#locate elem by heading "Selenium automates browsers. That's it!" by Xpath and print 
#locate elem by class 'selenium-backers' and print 

from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://wwww.selenium.dev')

htmlElem = driver.find_element_by_id('gsc-iw-id1')
print(htmlElem)


htmlElemName = driver.find_element_by_name('submit')
print(htmlElemName)


htmlElemXpath = driver.find_element_by_xpath('//*[@id="td-cover-block-0"]/div/div/div/div/h1')
print(htmlElemXpath)


classNameElem = driver.find_element_by_class_name('selenium-backers')
print(classNameElem)


driver.close()