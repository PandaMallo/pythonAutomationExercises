#https://wiki.python.org/moin/FrontPage
#search "Begginer"
#In the left menu, change value from 'More Options' to 'Raw Text'

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get('https://wiki.python.org/moin/FrontPage')

search = driver.find_element_by_id('searchinput')
search.clear()
search.send_keys('Begginer')
search.send_keys(Keys.RETURN)

select = Select(driver.find_element_by_xpath('//*/form/div/select'))
select.select_by_visible_text('Raw Text')

driver.close()