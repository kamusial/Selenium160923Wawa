from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https:/google.com')
time.sleep(1)
print('strona :',driver.title)

button1_accept = driver.find_element('id','L2AGLb')
button1_accept.click()
#driver.find_element('id','L2AGLb').click()   #to co wyżej, w jednej linii

search_field = driver.find_element('name', 'q')
search_field.send_keys('Ile lat ma Anna Lewandowska?')

search_button = driver.find_element('name', 'btnK')
search_button.submit()

time.sleep(1)
driver.quit()