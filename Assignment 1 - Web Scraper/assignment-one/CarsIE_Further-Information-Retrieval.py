import pandas as pd
import requests
from bs4 import BeautifulSoup

basic_page_url = "https://www.cars.ie/used-cars?page="

link_info_list = []
car_header_info = []
car_footer_info = []
car_price_info = []

TOTAL_PAGES = 2

for pageNumber in range(TOTAL_PAGES + 1):
    if(pageNumber == 0):
        continue


    # TODO: Retrieve the webpages based on these URLs (of 50 pages start with 5) and convert each into a beautifulsoup object
    url = basic_page_url + str(pageNumber)

    webpage = requests.get(url)

    webpage_content = webpage.text

    soup = BeautifulSoup(webpage_content, "html.parser")

    tables = soup.find_all("div", class_="car-listing-inner")

    table = tables[0]

    # TODO: Retrieve Car Manufacturing Year, Engine, Price, Dealer information (if it is available), and the URL (href) to access the detailed car information.

    for element in tables:

        if (element.name == '\n'):
            continue

        a_href_element = element.a

        href = "www.cars.ie" + a_href_element['href']

        link_info_list.append(href)

    # Get Header Info
    for element in tables:

        if (element.name == '\n'):
            continue

        header_info_blocks = element.find_all("h3", class_="greenText")

        header_info_block = header_info_blocks[0]

        car_header_info.append(header_info_block.text)

    # Get Footer Info
    for element in tables:

        if (element.name == '\n'):
            continue

        footer_info_blocks = element.find_all("p")

        footer_info_block = footer_info_blocks[0]

        car_footer_info.append(footer_info_block.text)

    # Get Price Info
    for element in tables:

        if (element.name == '\n'):
            continue

        price_info_blocks = element.find_all("p", class_="greenText price BP")

        price_info_block = price_info_blocks[0]

        car_price_info.append(price_info_block.text)

    print("Page Number = "+str(pageNumber))


# TODO: Save the information into a csv file
a = {'header': car_header_info, 'footer': car_footer_info, 'price': car_price_info, 'link': link_info_list}
df = pd.DataFrame.from_dict(a, orient='index')
df = pd.DataFrame.transpose(df)
df.to_csv("CarsIE-Simple_Information_Retrieval.csv")
# print(df)
'''
For Debugging
'''
# counter = 0
# for header, footer, price, link in zip(car_header_info, car_footer_info, car_price_info, link_info_list):
#     print("==> " + str(counter) + ") " + header + "\nCar Footer = " + footer + "Price = " + price + "\nLink = " + link + "\n")
#     counter+=1

car_url = "https://www.cars.ie/used-cars/MERCEDES-BENZ-E220-2005-Dublin-1616696"

page = requests.get(car_url)

page_content = page.text

s = BeautifulSoup(page_content, "html.parser")

car_tables = s.find_all("div", class_="col-sm-12 col-md-5")

car_table = car_tables[0]


a = 1
