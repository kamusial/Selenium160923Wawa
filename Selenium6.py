from selenium import webdriver
from Selenium4_class import LoginPage
import time
from Selenium2 import make_screenshot
import pytest

@pytest.mark.parametrize('username', ['standard_user', 'lockout_user'])
def test_login_page(username):   #parametr
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username(username)   #parametr
    page.enter_password('secret_sauce')
    page.click_login()
    time.sleep(1)
    try:
        assert driver.current_url == 'https://www.saucedemo.com/inventory.html', make_screenshot(driver)
        #jesli asercja sie nie uda, zrob screenshota
    except AssertionError:
        print('blad, zly adres')
        raise
    else:
        print('ok, dobry adres')
    finally:
        driver.quit()
