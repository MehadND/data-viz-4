import requests
from bs4 import BeautifulSoup
import pandas as pd

basic_url = "https://www.cars.ie/used-cars?page="

webpages = []

def cars_ie_scrap(webpage_text):

    soup = BeautifulSoup(webpage_text, "html.parser")

    tables = soup.find_all("div", class_="col-lg-4 col-md-12 car-listing")

    table = tables[0]

    car_info_list = []
    for element in tables:

        if (element.name == '\n'):
            continue

        a_element = element.a

        href = "www.cars.ie" + a_element['href']

        info_blocks = element.find_all("p", class_="greenText price BP")

        info_block = info_blocks[0]

        car_info = dict()
        car_info['href'] = href
        for it in info_block.contents:
            key = it
            value = it.text
            car_info[key] = value
        car_info_list.append(car_info)

    return car_info_list

car_info_list_all = []

for i in range(2):
    page_url = basic_url + str(i)

    webpages = requests.get(page_url).text

    car_info_list_per_page = cars_ie_scrap(webpages)

    car_info_list_all.extend(car_info_list_per_page)
    #webpages[i] = requests.get(page_url).text

df = pd.DataFrame.from_records(car_info_list_all)
df.to_csv("DoneDeal.csv")
print(df)

a = 1