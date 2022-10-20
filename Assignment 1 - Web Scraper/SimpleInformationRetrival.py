import requests
from bs4 import BeautifulSoup

TOTAL_PAGES = 3

basic_page_url = "https://www.cars.ie/used-cars?page="

all_pages_url = []
general_car_info_list = []
car_price_list = []


# TODO: Retrieve the webpages based on these URLs and convert each into a beautifulsoup object
def url_to_object(pageNumber, pageURL):
    all_pages_url.insert(pageNumber, pageURL)
    webpage = requests.get(pageURL).text

    soup = BeautifulSoup(webpage, "html.parser")

    general_car_info_list.insert(len(general_car_info_list), soup.find_all("div", class_="car-listing-footer"))


# TODO: Syntheses URLs to download the first 50 pages
def synthesis_url():
    for page in range(TOTAL_PAGES):
        if page == 0:
            continue
        else:
            page_url = basic_page_url + str(page)
            url_to_object(page, page_url)
            print(f"{page}: '" + page_url + "'\n")

    print("Synthesis of 50 URL completed...")


# TODO: Retrieve Car Manufacturing Year, Engine, Price, Dealer information (if it is available), and the URL (href)
#  to access the detailed car information.
def get_car_information_from_url(i):
    for car_info in general_car_info_list[i]:
        print(str(i)+" --> "+str(len(general_car_info_list)))
        info_blocks = car_info.find_all("p", class_="greenText price BP")
        car_price_list.append(info_blocks)
        if i > len(general_car_info_list):
            i = len(general_car_info_list) - 1
            continue
        else:
            i = i + 1

    # for car_info in general_car_info_list[i]:
    #     info_blocks = car_info.find_all("p", class_="greenText price BP")
    #     car_price_list.append(info_blocks)

    print("Get Car Information...")


# TODO: Save the information into a csv file
def saving_car_information_to_csv():
    for i in car_price_list:
        print(i.content)
    print("Saving Car Information completed...")


synthesis_url()
index = 0
get_car_information_from_url(index)

a = 1
