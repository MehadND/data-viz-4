import pandas as pd
import requests
from bs4 import BeautifulSoup

car_url = "https://www.cars.ie/used-cars/MERCEDES-BENZ-E220-2005-Dublin-1616696"

page = requests.get(car_url)

page_content = page.text

s = BeautifulSoup(page_content, "html.parser")

car_tables = s.find_all("div", class_="stripped-table")

car_table = car_tables[0]

rowList = []
for element in car_tables:

    if(element == '\n'):
        continue

    info = element.find_all("div", class_="row")
    rowList.append(info)

rowList_info_list = []
labels = []
data = []

for info in rowList[0]:
    if(info == '\n'):
        continue
    more_info = info.find_all("div", class_="col-xs-6")
    labels.append(more_info[0].text)
    data.append(more_info[1].text)

finalLabelList = []
for x in labels:
    if x == '\n':
        continue
    # print("Label == "+str(x).strip())
    finalLabelList.append(str(x).strip())


finalDataList = []
for x in data:
    if x == '\n':
        continue
    # print("Data == "+str(x).strip())
    finalDataList.append(str(x).strip())

a = {finalLabelList[0]: finalDataList}
df = pd.DataFrame.from_dict(a, orient='index')
df = pd.DataFrame.transpose(df)
df.to_csv("CarsIE-Further_Information_Retrieval.csv")

a = 1