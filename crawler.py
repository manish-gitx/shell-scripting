import requests
from bs4 import BeautifulSoup
import random


name=input()
URL=URL='https://www.amazon.in/s?k='+name+''
headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
resp = requests.get(URL, headers=headers)
resp=requests.get(URL,headers=headers)
soup=BeautifulSoup(resp.text,'html.parser')
info=[]
obj={}

links=soup.findAll('a',{'class':'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
for i in links:
    text='https://www.amazon.in/'+i.get('href')+''
    info.append(text)
    print(text)
    print()
    print()


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
for j in info:
    new_webpage = requests.get(j, headers=headers)
    new_soup = BeautifulSoup(new_webpage.text, "html.parser")
    try:
          info1 = new_soup.find('h1', {'id': 'title'}).text.strip()
          print(info1)
    except:
         print("not avaliable")




    




