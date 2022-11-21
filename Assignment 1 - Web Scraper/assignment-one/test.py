# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
#
# car_url = "https://www.cars.ie/used-cars/MERCEDES-BENZ-E220-2005-Dublin-1616696"
#
# page = requests.get(car_url)
#
# page_content = page.text
#
# s = BeautifulSoup(page_content, "html.parser")
#
# car_tables = s.find_all("div", class_="stripped-table")
#
# car_table = car_tables[0]
#
# rowList = []
# for element in car_tables:
#
#     if(element == '\n'):
#         continue
#
#     info = element.find_all("div", class_="row")
#     rowList.append(info)
#
# rowList_info_list = []
# labels = []
# data = []
#
# for info in rowList[0]:
#     if(info == '\n'):
#         continue
#     more_info = info.find_all("div", class_="col-xs-6")
#     labels.append(more_info[0].text)
#     data.append(more_info[1].text)
#
# finalLabelList = []
# for x in labels:
#     if x == '\n':
#         continue
#     # print("Label == "+str(x).strip())
#     finalLabelList.append(str(x).strip())
#
#
# finalDataList = []
# for x in data:
#     if x == '\n':
#         continue
#     # print("Data == "+str(x).strip())
#     finalDataList.append(str(x).strip())
#
# a = {finalLabelList[0]: finalDataList}
# df = pd.DataFrame.from_dict(a, orient='index')
# df = pd.DataFrame.transpose(df)
# df.to_csv("CarsIE-Further_Information_Retrieval.csv")
#
# a = 1

import time

import pandas as pd
import requests
from bs4 import BeautifulSoup

basic_page_url = "https://www.cars.ie/used-cars?page="

TOTAL_PAGES_TO_DOWNLOAD = 10

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
            url_to_object(url, str(page))


def url_to_object(pageURL, pageNumber):
    print("Page Number = " + pageNumber)
    webpage_content = requests.get(pageURL).text
    soup = BeautifulSoup(webpage_content, "html.parser")
    tables = soup.find_all("div", class_="car-listing-inner")
    objects_list.insert(len(objects_list), tables)

    print("Starting to getting data from page #" + pageNumber)
    get_car_link(tables)
    get_car_name(tables)
    get_car_price(tables)
    get_fuel_type(car_url_list)
    # get_colour(car_url_list)
    # get_engine_size(car_url_list)
    # get_transmission(car_url_list)
    # get_body_type(car_url_list)
    # get_number_of_prev_owners(car_url_list)
    # get_doors(car_url_list)
    # get_tax_expiry(car_url_list)
    # get_nct_expiry(car_url_list)
    get_manufacturing_year(tables)

    print("Finished getting data from page #" + pageNumber)