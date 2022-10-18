import os
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/mehad/Downloads/chromedriver_win32 (1)/chromedriver.exe')

driver.get("https://www.carzone.ie/used-cars/nissan/qashqai?make=Nissan&model=Qashqai")

source = driver.page_source

soup = BeautifulSoup(source, 'html.parser')

tables = soup.find_all('main', class_='stock-summary__details')

time.sleep(5)

driver.quit()

a = 1