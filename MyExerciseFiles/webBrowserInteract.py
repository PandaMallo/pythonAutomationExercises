from selenium import webdriver
driver = webdriver.Chrome()
driver.get('http://codepen.io/harunpehlivan/full/qBNpGKr')

#One input field
messageField = driver.find_element_by_xpath('//*[@id="editor"]/textarea')
messageField.send_key('print("Hello World!!")')
runButton= driver.find_element_by_xpath('//*[@id="run-btn"]')
runButton.click()


#Two input Fields
field1 = driver.find_element_by_xpath('xxx')
field1.send_key('x')
field1 = driver.find_element_by_xpath('yyy')
field1.send_key('y')
sendButton= driver.find_element_by_xpath('aaa')
sendButton.click()


