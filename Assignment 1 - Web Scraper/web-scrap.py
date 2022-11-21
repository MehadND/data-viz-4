import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

basic_page_url = "https://www.cars.ie/used-cars?page="

TOTAL_PAGES_TO_DOWNLOAD = 20

# objects_list = []
car_url_list = []
car_name_list = []
car_price_list = []
car_make_list = []
car_model_list = []
car_info_list = []
car_fuel_type_list = []
car_colour_list = []
car_engine_size_list = []
car_transmission_list = []
car_body_type_list = []
car_prev_owners_list = []
car_total_doors_list = []
car_tax_expiry_list = []
car_nct_expiry_list = []
car_year_list = []
car_odometer_list = []
car_county_list = []

for page in range(TOTAL_PAGES_TO_DOWNLOAD + 1):
    if page == 0:
        continue
    else:
        url = basic_page_url + str(page)
        print("Page Number = " + str(page))
        webpage_content = requests.get(url).text
        soup = BeautifulSoup(webpage_content, "html.parser")
        tables = soup.find_all("div", class_="car-listing-inner")

        for element in tables:
            if element == '\n':
                continue

            a_href_element = element.a

            href = "http://www.cars.ie" + a_href_element['href']

            car_url_list.append(href)

            info_blocks = element.find_all("h3", class_="greenText")

            info_block = info_blocks[0]

            car_name_list.append(info_block.text)

            car_make_list.append(str(info_block.text).split()[0])
            car_model_list.append(str(info_block.text).split()[1])

            info_blocks = element.find_all("p", class_="greenText price BP")

            info_block = info_blocks[0]

            car_price_list.append(info_block.text)

            info_blocks = element.find_all("div", class_="col-xs-10")

            info_block = info_blocks[0]

            car_year_list.append(str(info_block.text).split()[0])

            info_blocks = element.find_all("p", class_="text-right")

            info_block = info_blocks[0]

            car_county_list.append(str(info_block.text).split()[0])

for url in car_url_list:
    page = requests.get(url)

    page_content = page.text

    s = BeautifulSoup(page_content, "html.parser")

    car_tables = s.find_all("div", class_="stripped-table")

    # car_table = car_tables[0]
    car_info_list.append(car_tables)

    info_blocks = car_tables[0].find_all("div", class_="row")

    info_block = info_blocks[0]

    car_odometer_list.append(str(info_block.text).split()[3])

    info_block = info_blocks[1]

    car_fuel_type_list.append(str(info_block.text).split()[2])

    info_block = info_blocks[2]

    car_colour_list.append(str(info_block.text).split()[1])

    info_block = info_blocks[3]

    car_engine_size_list.append(str(info_block.text).split()[2])

    info_block = info_blocks[4]

    car_transmission_list.append(str(info_block.text).split()[1])

    info_block = info_blocks[5]

    car_body_type_list.append(str(info_block.text).split()[2])

    info_block = info_blocks[6]

    car_prev_owners_list.append(str(info_block.text).split()[1])

    info_block = info_blocks[7]

    car_total_doors_list.append(str(info_block.text).split()[1])

    info_block = info_blocks[8]

    car_tax_expiry_list.append(str(info_block.text).split()[2])

    info_block = info_blocks[9]

    car_nct_expiry_list.append(str(info_block.text).split()[2])

col_names = ['Name',
             'Price',
             'Model',
             'Make',
             'Fuel Type',
             'Odometer'
             'Colour',
             'Engine Size',
             'Transmission',
             'Body Type',
             'Manufacturing Year',
             'County',
             'Owners',
             'Doors',
             'Tax Expiry',
             'NCT Expiry',
             'Link'
             ]

print("Starting writing to csv file...")
a = {'Name': car_name_list, 'Price': car_price_list, 'Make': car_make_list, 'Model': car_model_list,
     'Fuel Type': car_fuel_type_list,
     'Odometer': car_odometer_list, 'Colour': car_colour_list, 'Engine Size ( in Litres)': car_engine_size_list,
     'Transmission': car_transmission_list,
     'Body Type': car_body_type_list, 'Manufacturing Year': car_year_list, 'County': car_county_list,
     'Owners': car_prev_owners_list, 'Doors': car_total_doors_list, 'Tax Expiry': car_tax_expiry_list,
     'NCT Expiry': car_nct_expiry_list, 'Link': car_url_list}

df = pd.DataFrame.from_dict(a, orient='index')
df = pd.DataFrame.transpose(df)
df.to_csv("CarsIE-Simple_Information_Retrieval.csv")
print("Finished writing to csv file")
df = pd.read_csv('CarsIE-Simple_Information_Retrieval.csv')
print(df)

a = 1
