import pandas as pd
import requests
from bs4 import BeautifulSoup

basic_page_url = "https://www.cars.ie/used-cars?page="

TOTAL_PAGES_TO_DOWNLOAD = 1

objects_list = []
car_url_list = []
car_name_list = []
car_price_list = []
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


def download_url():
    for page in range(TOTAL_PAGES_TO_DOWNLOAD + 1):
        if page == 0:
            continue
        else:
            url = basic_page_url + str(page)
            url_to_object(url)


def url_to_object(pageURL):
    webpage_content = requests.get(pageURL).text
    soup = BeautifulSoup(webpage_content, "html.parser")
    tables = soup.find_all("div", class_="car-listing-inner")
    objects_list.insert(len(objects_list), tables)

    get_car_link(tables)
    get_car_name(tables)
    get_car_price(tables)
    get_fuel_type(car_url_list)
    get_colour(car_url_list)
    get_engine_size(car_url_list)
    get_transmission(car_url_list)
    get_body_type(car_url_list)
    get_number_of_prev_owners(car_url_list)
    get_doors(car_url_list)
    get_tax_expiry(car_url_list)
    get_nct_expiry(car_url_list)
    get_manufacturing_year(tables)
    save_to_csv()


def get_car_link(tables):
    for element in tables:
        if element == '\n':
            continue

        a_href_element = element.a

        href = "http://www.cars.ie" + a_href_element['href']

        car_url_list.append(href)


def get_car_name(tables):
    for element in tables:
        if element.name == '\n':
            continue

        info_blocks = element.find_all("h3", class_="greenText")

        info_block = info_blocks[0]

        car_name_list.append(info_block.text)


def get_car_price(tables):
    for element in tables:
        if element.name == '\n':
            continue

        info_blocks = element.find_all("p", class_="greenText price BP")

        info_block = info_blocks[0]

        car_price_list.append(info_block.text)


def get_car_make():
    pass


def get_car_model():
    pass


def get_fuel_type(carURLList):
    for car_url in carURLList:
        page = requests.get(car_url)

        page_content = page.text

        s = BeautifulSoup(page_content, "html.parser")

        car_tables = s.find_all("div", class_="stripped-table")

        car_table = car_tables[0]
        car_info_list.append(car_table)

        info_blocks = car_table.find_all("div", class_="row")

        info_block = info_blocks[1]

        car_fuel_type_list.append(str(info_block.text).split()[2])


def get_colour(carURLList):
    for car_url in carURLList:
        page = requests.get(car_url)

        page_content = page.text

        s = BeautifulSoup(page_content, "html.parser")

        car_tables = s.find_all("div", class_="stripped-table")

        car_table = car_tables[0]
        car_info_list.append(car_table)

        info_blocks = car_table.find_all("div", class_="row")

        info_block = info_blocks[2]

        car_colour_list.append(str(info_block.text).split()[1])


def get_engine_size(carURLList):
    for car_url in carURLList:
        page = requests.get(car_url)

        page_content = page.text

        s = BeautifulSoup(page_content, "html.parser")

        car_tables = s.find_all("div", class_="stripped-table")

        car_table = car_tables[0]
        car_info_list.append(car_table)

        info_blocks = car_table.find_all("div", class_="row")

        info_block = info_blocks[3]

        car_engine_size_list.append(str(info_block.text).split()[2])


def get_transmission(carURLList):
    for car_url in carURLList:
        page = requests.get(car_url)

        page_content = page.text

        s = BeautifulSoup(page_content, "html.parser")

        car_tables = s.find_all("div", class_="stripped-table")

        car_table = car_tables[0]
        car_info_list.append(car_table)

        info_blocks = car_table.find_all("div", class_="row")

        info_block = info_blocks[4]

        car_transmission_list.append(str(info_block.text).split()[1])


def get_body_type(carURLList):
    for car_url in carURLList:
        page = requests.get(car_url)

        page_content = page.text

        s = BeautifulSoup(page_content, "html.parser")

        car_tables = s.find_all("div", class_="stripped-table")

        car_table = car_tables[0]
        car_info_list.append(car_table)

        info_blocks = car_table.find_all("div", class_="row")

        info_block = info_blocks[5]

        car_body_type_list.append(str(info_block.text).split()[2])


def get_number_of_prev_owners(carURLList):
    for car_url in carURLList:
        page = requests.get(car_url)

        page_content = page.text

        s = BeautifulSoup(page_content, "html.parser")

        car_tables = s.find_all("div", class_="stripped-table")

        car_table = car_tables[0]
        car_info_list.append(car_table)

        info_blocks = car_table.find_all("div", class_="row")

        info_block = info_blocks[6]

        car_prev_owners_list.append(str(info_block.text).split()[1])


def get_doors(carURLList):
    for car_url in carURLList:
        page = requests.get(car_url)

        page_content = page.text

        s = BeautifulSoup(page_content, "html.parser")

        car_tables = s.find_all("div", class_="stripped-table")

        car_table = car_tables[0]
        car_info_list.append(car_table)

        info_blocks = car_table.find_all("div", class_="row")

        info_block = info_blocks[7]

        car_total_doors_list.append(str(info_block.text).split()[1])


def get_tax_expiry(carURLList):
    for car_url in carURLList:
        page = requests.get(car_url)

        page_content = page.text

        s = BeautifulSoup(page_content, "html.parser")

        car_tables = s.find_all("div", class_="stripped-table")

        car_table = car_tables[0]
        car_info_list.append(car_table)

        info_blocks = car_table.find_all("div", class_="row")

        info_block = info_blocks[8]

        car_tax_expiry_list.append(str(info_block.text).split()[2])


def get_nct_expiry(carURLList):
    for car_url in carURLList:
        page = requests.get(car_url)

        page_content = page.text

        s = BeautifulSoup(page_content, "html.parser")

        car_tables = s.find_all("div", class_="stripped-table")

        car_table = car_tables[0]
        car_info_list.append(car_table)

        info_blocks = car_table.find_all("div", class_="row")

        info_block = info_blocks[9]

        car_nct_expiry_list.append(str(info_block.text).split()[2])


def get_manufacturing_year(tables):
    for element in tables:
        if element.name == '\n':
            continue

        info_blocks = element.find_all("div", class_="col-xs-10")

        info_block = info_blocks[0]

        car_year_list.append(str(info_block.text).split()[0])


def save_to_csv():
    a = {'Name': car_name_list, 'Price': car_price_list, 'Make': '', 'Model': '', 'Manufacturing Year': '',  'Country': '', 'Fuel Type': car_fuel_type_list, 'Colour': car_colour_list, 'Engine Size': car_engine_size_list, 'Transmission': car_transmission_list, 'Body Type': car_body_type_list, 'Owners': car_prev_owners_list, 'Doors': car_total_doors_list, 'Tax Expiry': car_tax_expiry_list, 'NCT Expiry': car_nct_expiry_list, 'Link': car_url_list}
    df = pd.DataFrame.from_dict(a, orient='index')
    df = pd.DataFrame.transpose(df)
    df.to_csv("CarsIE-Simple_Information_Retrieval.csv")
    # print(df)




# for pageNumber in range(TOTAL_PAGES_TO_DOWNLOAD + 1):
#     if(pageNumber == 0):
#         continue
#
#
#     # TODO: Retrieve the webpages based on these URLs (of 50 pages start with 5) and convert each into a beautifulsoup object
#     url = basic_page_url + str(pageNumber)
#
#     webpage = requests.get(url)
#
#     webpage_content = webpage.text
#
#     soup = BeautifulSoup(webpage_content, "html.parser")
#
#     tables = soup.find_all("div", class_="car-listing-inner")
#
#     table = tables[0]
#
#     # TODO: Retrieve Car Manufacturing Year, Engine, Price, Dealer information (if it is available), and the URL (href) to access the detailed car information.
#
#     for element in tables:
#
#         if (element.name == '\n'):
#             continue
#
#         a_href_element = element.a
#
#         href = "www.cars.ie" + a_href_element['href']
#
#         link_info_list.append(href)
#
#     # Get Header Info
#     for element in tables:
#
#         if (element.name == '\n'):
#             continue
#
#         header_info_blocks = element.find_all("h3", class_="greenText")
#
#         header_info_block = header_info_blocks[0]
#
#         car_header_info.append(header_info_block.text)
#
#     # Get Footer Info
#     for element in tables:
#
#         if (element.name == '\n'):
#             continue
#
#         footer_info_blocks = element.find_all("p")
#
#         footer_info_block = footer_info_blocks[0]
#
#         car_footer_info.append(footer_info_block.text)
#
#     # Get Price Info
#     for element in tables:
#
#         if (element.name == '\n'):
#             continue
#
#         price_info_blocks = element.find_all("p", class_="greenText price BP")
#
#         price_info_block = price_info_blocks[0]
#
#         car_price_info.append(price_info_block.text)
#
#     print("Page Number = "+str(pageNumber))
#
#
# # TODO: Save the information into a csv file
# a = {'header': car_header_info, 'footer': car_footer_info, 'price': car_price_info, 'link': link_info_list}
# df = pd.DataFrame.from_dict(a, orient='index')
# df = pd.DataFrame.transpose(df)
# df.to_csv("CarsIE-Simple_Information_Retrieval.csv")
# # print(df)
# '''
# For Debugging
# '''
# # counter = 0
# # for header, footer, price, link in zip(car_header_info, car_footer_info, car_price_info, link_info_list):
# #     print("==> " + str(counter) + ") " + header + "\nCar Footer = " + footer + "Price = " + price + "\nLink = " + link + "\n")
# #     counter+=1

download_url()
# get_car_information_simple()
a = 1
