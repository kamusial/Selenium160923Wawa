from selenium import webdriver
from Selenium4_class import LoginPage
import time
from Selenium2 import make_screenshot
import pytest

test_data = [
    ('standard_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('locked_out_user', 'secret_sauce', 'https://www.saucedemo.com/'),
    ('problem_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html'),
    ('performance_glitch_user', 'secret_sauce', 'https://www.saucedemo.com/inventory.html')
]

@pytest.mark.parametrize('username, password, url', test_data)
def test_login_page(username, password, url):   #parametr
    driver = webdriver.Chrome()
    page = LoginPage(driver)
    page.open()
    page.enter_username(username)   #parametr
    page.enter_password(password)
    page.click_login()
    time.sleep(1)
    try:
        assert driver.current_url == url, make_screenshot(driver)
        #jesli asercja sie nie uda, zrob screenshota
    except AssertionError:
        print('blad, zly adres')
        raise
    else:
        print('ok, dobry adres')
    finally:
        driver.quit()
