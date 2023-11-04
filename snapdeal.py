import requests
from bs4 import BeautifulSoup
import random
from prettytable import PrettyTable


name=input()

URL='https://www.snapdeal.com/search?keyword='+name+''
headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
resp = requests.get(URL, headers=headers)
soup=BeautifulSoup(resp.text,'html.parser')
step1=soup.find('div',{'id':'products'})
step2=step1.findAll('a',{'class':'dp-widget-link'})





def name(soup):
    try:
        name=soup.find('h1',{"class":"pdp-e-i-head"}).text.strip()
        return name
    except:
        print("N/A")

def price(soup):
    try:
        name=soup.find('span',{"class":"pdp-final-price"}).text.strip()
        return name
    except:
        print("N/A")



    



for j in step2:
    snap_link=j.get('href')
    snapd_webpage = requests.get(snap_link, headers=headers)
    newd_soup = BeautifulSoup(snapd_webpage.text, "html.parser")
    snapd_name=name(newd_soup)
    snapd_price=price(newd_soup)
    print(snapd_name)
    print(snapd_price)
    print()
