from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#browser = webdriver.Chrome()
#browser.get('http://www.seleniumhq.org')

driver = webdriver.Chrome()
driver.get('http://www.python.org')

elem = driver.find_element_by_name('q')
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
time.sleep(8)

driver.close()

