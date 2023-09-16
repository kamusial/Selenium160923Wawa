from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
print('Nazwa strony',driver.title)

username_field = driver.find_element('id','user-name')
username_field.clear()
username_field.send_keys('standard_user')

password_field = driver.find_element('xpath','//*[@id="password"]')
username_field.clear()
password_field.send_keys('secret_sauce')

login_button = driver.find_element('name', 'login-button')
if not login_button.get_attribute('disabled'):    #czy przycisk aktywny
    login_button.click()

def make_screenshot(okno_przegladarki):
    today = datetime.datetime.today()
    short_date = today.strftime('_stamp%H%M%S')
    screen_name = 'screen' + short_date + '.png'
    okno_przegladarki.get_screenshot_as_file(screen_name)

driver.quit()

