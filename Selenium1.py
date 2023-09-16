from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https:/google.com')
time.sleep(1)
print('strona :',driver.title)
button1_accept = driver.find_element('id','L2AGLb')
# print(button1_accept)
# print(type(button1_accept))

button1_accept.click()
time.sleep(1)
driver.quit()