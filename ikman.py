# requesting inforematopn from website

from bs4 import BeautifulSoup
from numpy import dtype
import requests

html_text = requests.get("https://ikman.lk/en/ads/sri-lanka/computers-tablets?sort=date&order=desc&buy_now=0&urgent=0&type=for_sale&page=1").text # web site we get informaton  / .text  because we only accept text

soup = BeautifulSoup(html_text,"lxml")



adds = soup.find_all("li", { "class":"normal--2QYVk gtm-normal-ad"})

# Get text from each tag
for add in adds:
    Item = add.find("h2","heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow").text
    District = add.find("div","description--2-ez3").text.split(",")[0]
    Price = add.find("div","price--3SnqI color--t0tGX").text
    info = add.a["href"]
    if District == "Colombo": 
        print(f"Item name : {Item.strip()}")
        print(f"price : {Price.strip()}")
        print(f"more info : https//ikman.lk{info}")