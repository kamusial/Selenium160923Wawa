from selenium import webdriver
from Selenium4_class import LoginPage
import time
from Selenium2 import make_screenshot

driver = webdriver.Chrome()
page = LoginPage(driver)
page.open()
page.enter_username('standard_user')
page.enter_password('secret_sauce')
page.click_login()
time.sleep(1)
try:
    assert driver.current_url == 'https://www.saucedemo.com/inventory.htmlw', make_screenshot(driver)
    #jesli asercja sie nie uda, zrob screenshota
except AssertionError:
    print('blad, zly adres')
    raise
else:
    print('ok, dobry adres')
finally:
    driver.quit()
