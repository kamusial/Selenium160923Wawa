from selenium import webdriver
from Selenium4_class import LoginPage
import time
from Selenium2 import make_screenshot
import pytest

#headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get('http://www.allegro.pl')
time.sleep(1)
driver.quit()


#przejście do drugiej karty
currentWindowName = driver.current_window_handle   #nazwa karty
windowNames = driver.window_handles   #nazwy wszystkich kart
#print(windowNames)

for okno in windowNames:
    if okno != currentWindowName:
        driver.switch_to.window(okno)
