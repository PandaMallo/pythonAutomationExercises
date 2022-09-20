from selenium import webdriver
import time
#For serchbox
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://python.org')

##Search in the searchbox
search = driver.find_element_by_name('q')
#Clean serchbox if it has content
search.clear()
#Search what ever
search.send_keys('pycon')
#press enter
search.send_keys(Keys.RETURN)
time.sleep(4)

driver.close()

##-------------------------------------------------------------
#For forms
from selenium.webdriver.support.ui import Select
driver.get('http://www.......com')

##Form interaction
select = Select(driver.find_element_by_class_name('select_ele_form'))
select.select_by_index('ex_num')
time.sleep(2)
select.select_by_visible_text('ex_num/text')
time.sleep(2)
select.select_by_value('ex_num/text')
time.sleep(2)

options =select.options
print(options)

submit_button = driver.find_element_by_name('continue')
submit_button.submit()
time.sleep(2)

driver.close()

##-------------------------------------------------------------
#For Drag and drop
from selenium.webdriver import ActionChains
driver.get('http://jqueryui.com/droppable')
driver.switch_to.frame(0)

action_chains = ActionChains(driver)

source = driver.find_element_by_id('draggable')
target = driver.find_element_by_id('droppable')

action_chains.drag_and_drop_by_offset(source, 100, 100).perform()
time.sleep(2)
action_chains.drag_and_drop_by_offset(source, target).perform()
time.sleep(2)

driver.close()
