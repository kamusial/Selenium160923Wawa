from selenium import webdriver
import time

okno1 = webdriver.Chrome()
okno1.get('https:/google.com')
time.sleep(1)

okno2 = webdriver.Chrome()
okno2.get('https:/allegro.pl')
time.sleep(1)

okno3 = webdriver.Chrome()
okno3.get('https:/google.com')
time.sleep(1)

okno1.quit()
okno2.quit()
okno3.quit()