from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.common.exceptions import NoSuchElementException

def make_screenshot(driver):
    today = datetime.datetime.today()
    short_date = today.strftime('_stamp%H%M%S')
    screen_name = 'screen' + short_date + '.png'
    driver.get_screenshot_as_file(screen_name)

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    print('Nazwa strony',driver.title)

    try:
        username_field = driver.find_element('id', 'user-name')
    except:
        print('nie znaleziono, szukam standardowych credentiali')
        username_field = driver.find_element('id', 'user-name')
        make_screenshot(driver)

    username_field.clear()
    username_field.send_keys('standard_user')

    try:
        password_field = driver.find_element(By.XPATH,'//*[@id="password"]')
    except NoSuchElementException:
        make_screenshot(driver)
        print('Nie znaleziono pola z haslem')
        raise

    username_field.clear()
    password_field.send_keys('secret_sauce')

    login_button = driver.find_element('name', 'login-button')
    if not login_button.get_attribute('disabled'):    #czy przycisk aktywny
        login_button.click()

    make_screenshot(driver)

    driver.quit()


