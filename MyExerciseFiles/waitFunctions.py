from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

url = 'https://earth.google.com/web/@-47.81006976,72.51238361,-8375.66482587a,22040242.23069906d,35y,43.49143162h,27.89109545t,0r'
driver = webdriver.Chrome()
driver.get(url)
wait = WebDriverWait(driver, 10)
constelationButton = wait.until(EC.element_to_be_clickable((By.PATH, '//*[@id="icon"]')))
constelationButton.click()
