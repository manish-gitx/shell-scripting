import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent
from prettytable import PrettyTable

URL='https://www.reliancedigital.in/search?q=iphone 15:relevance'
headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
resp = requests.get(URL, headers=headers)
soup=BeautifulSoup(resp.text,'html.parser')
info1=[]
links=soup.find('div',{"class":"pl__container"})
allLinks=links.find_all('a')
for i in allLinks:
    text='https://www.reliancedigital.in'+i.get('href')+''
    info1.append(text)

def title1(soup):
    try:
        info1 = soup.find('h1', {'class': 'pdp__title'}).text.strip()
        return info1
    except:
        return "N/A"

def price1(soup):
    try:
        price=soup.find("li",{"class":"pdp__priceSection__priceListText"}).text.strip()
        return(price)

    except:
       return "N/A"

table = PrettyTable()
table.field_names = ["Product Name", "Price"]

for j in info1:
    new_webpage = requests.get(j, headers=headers)
    new_soup = BeautifulSoup(new_webpage.text, "html.parser")
    product_name = title1(new_soup)
    product_price = price1(new_soup)
    table.add_row([product_name, product_price])

print(table)
