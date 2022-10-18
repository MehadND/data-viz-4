import requests
from bs4 import BeautifulSoup

url = "https://www.carzone.ie/search" 
webpage = requests.get(url)

webpage_text = webpage.text

soup = BeautifulSoup(webpage_text, "html.parser")




a = 1