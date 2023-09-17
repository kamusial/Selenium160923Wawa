#Page Object Model
from selenium.webdriver.common.by import By
from selenium import webdriver

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field_id = 'user-name'
        self.password_field_id = 'password'
        self.login_button_name = 'login-button'

    def open(self):
        self.driver.get('http://www.saucedemo.com')
        self.driver.maximize_window()

    def enter_username(self, username):
        field = self.driver.find_element(By.ID, self.username_field_id)
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.driver.find_element(By.ID, self.password_field_id)
        field.clear()
        field.send_keys(password)

    def click_login(self):
        button = self.driver.find_element('name', self.login_button_name)
        button.click()