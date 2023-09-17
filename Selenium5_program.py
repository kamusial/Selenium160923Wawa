from selenium import webdriver
from Selenium4_class import LoginPage

driver = webdriver.Chrome()

page = LoginPage(driver)
page.open()
page.enter_username('standard_user')
page.enter_password('secret_sauce')


driver.quit()