from selenium import webdriver
import time
import selenium.webdriver.support.ui as UI

driver = webdriver.Chrome()
# Open the desired web page
driver.get('http://juliemr.github.io/protractor-demo/')

# Type in numbers for operation
first_number = driver.find_element_by_css_selector('[ng-model=first]')
first_number.send_keys('25')
second_number = driver.find_element_by_css_selector('[ng-model=second]')
second_number.send_keys('42')

# Select the operation to be performed
operation_add = UI.Select(driver.find_element_by_css_selector('[ng-model=operator]')).select_by_value("ADDITION")

# Click on the button to perform operation
result_button = driver.find_element_by_class_name('btn')
result_button.click()

# Await operation to be performed
time.sleep(4)
result = driver.find_element_by_class_name('ng-binding')

# Assert operation result and finish browser instance
assert result.text == '67'
driver.quit()