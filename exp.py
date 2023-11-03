import requests
from bs4 import BeautifulSoup
import random


URL='https://www.amazon.in//Apple-iPhone-15-256-GB/dp/B0CHX4CRND/ref=sr_1_15?keywords=iphone+15&qid=1698977754&sr=8-15'
headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
resp = requests.get(URL, headers=headers)
soup=BeautifulSoup(resp.text,'html.parser')
info1 = soup.find('h1', {'id': 'title'}).text.strip()
print(info1)