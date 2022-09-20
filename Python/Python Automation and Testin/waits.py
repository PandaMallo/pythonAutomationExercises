from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://python.org')

#Explicit Wait
try:
    elm =WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'start-shell')))
finally:
    driver.quit()


#Implicit Wait(every call of every element)
driver.implicitly_wait(10) #seconds

myDynamicElm = driver.find_element_by_id('start-shell')

driver.close()
