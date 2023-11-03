import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from fake_useragent import UserAgent

URL='https://www.reliancedigital.in/search?q=iphone 15:relevance'
headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
resp = requests.get(URL, headers=headers)
soup=BeautifulSoup(resp.text,'html.parser')
info=[]
links=soup.find('div',{"class":"pl__container"})
allLinks=links.find_all('a')
for i in allLinks:
    text='https://www.reliancedigital.in'+i.get('href')+''
    info.append(text)
def title(soup):
    try:
        info1 = soup.find('h1', {'class': 'pdp__title'}).text.strip()
        return info1
    except:
        return "N/A"

def price(soup):
    try:
        price=soup.find("li",{"class":"pdp__priceSection__priceListText"}).text.strip()
        return(price)

    except:
       return "N/A"

for j in info:
    new_webpage = requests.get(j, headers=headers)
    new_soup = BeautifulSoup(new_webpage.text, "html.parser")
    print(title(new_soup))
    print(price(new_soup))
    
    print()



# count=0
# info=[]
# for i in links:
#     text='https://www.reliancedigital.in/'+i.get('href')+''
#     info.append(text)
# for i in info:
#     print(info)


# def get_product_info(url):
#     headers = {"accept-language": "en-US,en;q=0.9", "accept-encoding": "gzip, deflate, br"}
#     with requests.Session() as session:
#         session.headers.update(headers)
#         response = session.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         try:
#             title = soup.find('h1', {'id': 'title'}).text.strip()
#         except:
#             title = "not available"
#         try:
#             price = soup.find("span", {"class": "a-price"}).find("span").text
#         except:
#             price = "not available"
#         return title, price


# if __name__ == '__main__':
#     name = input()
#     url = f'https://www.amazon.in/s?k={name}'
#     ua = UserAgent()
#     headers = {"User-Agent": ua.random}
#     with requests.Session() as session:
#         session.headers.update(headers)
#         response = session.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#         links = soup.findAll('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
#         links = ['https://www.amazon.in/' + i.get('href') for i in links][:10]
#         with ThreadPoolExecutor(max_workers=10) as executor:
#             results = executor.map(get_product_info, links)
#         for title, price in results:
#             print(title)
#             print(price)
#             print()
