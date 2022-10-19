from bs4 import BeautifulSoup
import requests

url = "https://www.cars.ie/used-cars"

webpage = requests.get(url)

webpage_text = webpage.text

soup = BeautifulSoup(webpage_text, "html.parser")

tables = soup.find_all("div", class_="col-lg-4 col-md-12 car-listing")

table = tables[0]

car_info_list = []
for element in tables:

    if(element.name == '\n'):
        continue

    a_element = element.a

    href = "www.cars.ie" + a_element['href']

    info_blocks = element.find_all("div", class_="car-listing-footer")

    info_block = info_blocks[0]

    car_info = dict()
    car_info['href'] = href
    for it in info_block.contents:
        key = it
        value = it.text
        car_info[key] = value
    car_info_list.append(car_info)

a = 1