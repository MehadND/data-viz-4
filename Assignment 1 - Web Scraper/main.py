import os
import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver

driver = webdriver.Chrome('C:/Users/mehad/Downloads/chromedriver_win32 (1)/chromedriver.exe')

driver.get(f"https://www.carzone.ie/used-cars/nissan/qashqai?make=Nissan&model=Qashqai&page=1")

source = driver.page_source

soup = BeautifulSoup(source, 'html.parser')

tables = soup.find_all('main', class_='stock-summary__details')

table = tables[0]

val = table.contents[0]

# print(val.contents)

car_info = dict()
car_info_list = []
for v in val:

    for it in val.contents:
        key = it
        value = it.text
        car_info[key] = value
    car_info_list.append(car_info)

a = 1