import pandas as pd
import requests
from bs4 import BeautifulSoup

TOTAL_PAGES = 4

basic_page_url = "https://www.cars.ie/used-cars?page="

all_pages_url = []
general_car_info_list = []
car_price_list = []
car_year_list = []
car_make_ist = []
car_model_ist = []

element_list = []


# TODO: Retrieve the webpages based on these URLs and convert each into a beautifulsoup object
def url_to_object(pageNumber, pageURL):
    all_pages_url.insert(pageNumber, pageURL)
    webpage = requests.get(pageURL).text

    soup = BeautifulSoup(webpage, "html.parser")

    general_car_info_list.insert(len(general_car_info_list), soup.find_all("div", class_="car-listing-footer"))
    element_list.insert(len(general_car_info_list), soup.find_all("div", class_="car-listing-header"))


# TODO: Syntheses URLs to download the first 50 pages
def synthesis_url():
    for page in range(TOTAL_PAGES):
        if page == 0:
            continue
        else:
            page_url = basic_page_url + str(page)
            url_to_object(page, page_url)
            print(f"{page}: '" + page_url + "'\n")

    # print("Synthesis of 50 URL completed...")


# TODO: Retrieve Car Manufacturing Year, Engine, Price, Dealer information (if it is available), and the URL (href)
#  to access the detailed car information.
def get_car_information_from_url(i):
    for car_info in general_car_info_list[i]:
        info_blocks = car_info.find_all("p", class_="greenText price BP")
        car_price_list.append(info_blocks)
        # element = info_blocks.find_all("div", class_="col-xs-10")
        # element_list.append(element)

    if i < (len(general_car_info_list) - 1):
        i = i + 1
        get_car_information_from_url(i)

    # print("Get Car Information...")


# TODO: Save the information into a csv file
def saving_car_information_to_csv():
    print("Saving Car Information completed...")


stringPrice = []


# TODO: Get Price
def get_car_price(i):
    for car_info in general_car_info_list[i]:
        info_blocks = car_info.find_all("p", class_="greenText price BP")
        car_price_list.append(info_blocks)
        # element = info_blocks.find_all("div", class_="col-xs-10")
        # element_list.append(element)
        stringPrice.insert(len(general_car_info_list), str(car_price_list[i]).split())

    if i < (len(general_car_info_list) - 1):
        i = i + 1
        get_car_price(i)

    for price in car_price_list:
        # stringPrice.append(str(price[0].text).split()[0])
        print(price)


year_list = []
make_list = []
model_list = []


# TODO: Get Manufacturing Year
def get_car_year(i):
    for car_info in general_car_info_list[i]:
        info_blocks = car_info.find_all("p")
        car_year_list.append(info_blocks)
        # element = info_blocks.find_all("div", class_="col-xs-10")
        # element_list.append(element)
        #year_list.insert(len(general_car_info_list), car_year_list[i].split())

    if i < (len(general_car_info_list) - 1):
        i = i + 1
        get_car_year(i)

    for car in car_year_list:
        print(car)


def get_car_make(i):
    for carInformation in element_list[i]:
        info = carInformation.find("h3")
        car_make_ist.append(info)
        # element = info_blocks.find_all("div", class_="col-xs-10")
        # element_list.append(element)
        make_list.insert(len(element_list), str(car_make_ist[i].text).split()[0])

    if i < (len(element_list) - 1):
        i = i + 1
        get_car_make(i)

    for car in car_make_ist:
        # model_list.append(str(car[1].text).split()[1])
        # make_list.append()
        print(car)


def get_car_model(i):
    for carInformation in element_list[i]:
        info = carInformation.find("h3")
        car_model_ist.append(info)
        # element = info_blocks.find_all("div", class_="col-xs-10")
        # element_list.append(element)
        model_list.insert(len(element_list), str(car_model_ist[i].text).split()[1])

    if i < (len(element_list) - 1):
        i = i + 1
        get_car_model(i)

    # for i in car_model_ist:
    # model_list.append()
    # print(i)


synthesis_url()

index = 0
# get_car_information_from_url(index)
get_car_price(index)

index = 0
get_car_year(index)

index = 0
get_car_make(index)

index = 0
get_car_model(index)

a = {'Year': year_list, 'Make': car_make_ist, 'Model': car_model_ist, 'Price': car_price_list}
df = pd.DataFrame.from_dict(a, orient='index')
df.to_csv("Cars_IE.csv")
df = df.transpose()
print(df)

print()
# df = pd.DataFrame({'Year': car_year_list,
#                    'Price': car_price_list})
# df.to_csv("DoneDeal.csv")
# print(df)

a = 1
