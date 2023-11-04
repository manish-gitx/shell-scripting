import requests
from bs4 import BeautifulSoup
import random
from prettytable import PrettyTable


name=input()
URL='https://www.amazon.in/s?k='+name+''
URL1='https://www.reliancedigital.in/search?q='+name+':relevance'
headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
resp = requests.get(URL, headers=headers)
resp1=requests.get(URL1,headers=headers)
soup1=BeautifulSoup(resp1.text,'html.parser')
soup=BeautifulSoup(resp.text,'html.parser')

info1=[]
info=[]
name=[]
obj={}

links=soup.findAll('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
count=0
for i in links:
    if(count==10):
        break
    text='https://www.amazon.in/'+i.get('href')+''
    info.append(text)
    count=count+1


# for j in info:
#     URL1 = j
#     resp1 = requests.get(URL1, headers=headers)
#     soup1 = BeautifulSoup(resp1.text, 'html.parser')
#     try:
#         info1 = soup1.find('span', {'id': 'productTitle'})  # Update the class or ID as per the Amazon HTML structure
#         if info1:
#             print(info1.text.strip())
#         else:
#             print("Title not found")
#     except Exception as e:
#         print("An error occurred:", e)
def title(soup):
    try:
        info1 = soup.find('h1', {'id': 'title'}).text.strip()
        return info1
    except:
        return "N/A"

def price(soup):
    try:
        price=soup.find("span",{"class":"a-price-whole"}).text.strip()
        return(price)

    except:
       return "N/A"
    
table = PrettyTable()
table.field_names = ["Product Name", "Price"]

             
for j in info:
    new_webpage = requests.get(j, headers=headers)
    new_soup = BeautifulSoup(new_webpage.text, "html.parser")
    product_name = title(new_soup)
    product_price = price(new_soup)
    table.add_row([product_name, product_price])
    
print(table)

print("REALINCE DIGITAL---------------------------")
links=soup1.find('div',{"class":"pl__container"})
try:
    allLinks=links.find_all('a')
except:
    print("results N/A")


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
table1 = PrettyTable()
table1.field_names = ["Product Name", "Price"]
for j in info1:
    new_webpage = requests.get(j, headers=headers)
    new_soup = BeautifulSoup(new_webpage.text, "html.parser")
    product_name1 = title1(new_soup)
    product_price1 = price1(new_soup)
    table1.add_row([product_name1, product_price1])

    
print(table1)













    




