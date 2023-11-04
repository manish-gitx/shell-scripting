import requests
from bs4 import BeautifulSoup
import random
import requests
from prettytable import PrettyTable
from bs4 import BeautifulSoup

name = input()
URL2 = 'https://www.snapdeal.com/search?keyword=' + name

headers = {
    "accept-language": "en-US,en;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

resp2 = requests.get(URL2, headers=headers)
soup2 = BeautifulSoup(resp2.content, "html.parser")
step1 = soup2.find('div', {'id': 'products'})
step2 = step1.findAll('a', {'class': 'dp-widget-link'})

table2 = PrettyTable()
table2.field_names = ["Product Name", "Price"]


def namesnap(soup):
    try:
        namesnap = soup.find('h1', {"class": "pdp-e-i-head"}).text.strip()
        return namesnap
    except:
        return "N/A"


def pricesnap(soup):
    try:
        nameprice = soup.find('span', {"class": "pdp-final-price"}).text.strip()
        return nameprice
    except:
        return "N/A"


for j in step2:
    snap_link = j.get('href')
    snapd_webpage = requests.get(snap_link, headers=headers)
    newd_soup = BeautifulSoup(snapd_webpage.content, "html.parser")
    snapd_name = namesnap(newd_soup)
    snapd_price = pricesnap(newd_soup)
    table2.add_row([snapd_name, snapd_price])

print(table2)






