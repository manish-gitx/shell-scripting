import requests
from bs4 import BeautifulSoup
import concurrent.futures
import tkinter as tk


def scrape_amazon(name):
    URL = f'https://www.amazon.in/s?k={name}'
    headers = {
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }
    resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    links = soup.findAll('a', {'class': 'a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal'})
    links = [f'https://www.amazon.in/{i.get("href")}' for i in links[:10]]

    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(scrape_amazon_product, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    return results


def scrape_amazon_product(link, headers):
    result = {}
    resp = requests.get(link, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    result['title'] = soup.find('h1', {'id': 'title'}).text.strip() if soup.find('h1', {'id': 'title'}) else 'N/A'
    result['price'] = soup.find("span", {"class": "a-price"}).find("span").text.strip() if soup.find("span", {"class": "a-price"}) else 'N/A'

    return result


def scrape_reliance(name):
    URL = f'https://www.reliancedigital.in/search?q={name}:relevance'
    headers = {
        "accept-language": "en-US,en;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
    }
    resp = requests.get(URL, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    links = soup.find('div', {"class": "pl__container"}).find_all('a')
    links = [f'https://www.reliancedigital.in{i.get("href")}' for i in links]

    results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(scrape_reliance_product, link, headers) for link in links]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    return results


def scrape_reliance_product(link, headers):
    result = {}
    resp = requests.get(link, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')

    result['title'] = soup.find('h1', {'class': 'pdp__title'}).text.strip() if soup.find('h1', {'class': 'pdp__title'}) else 'N/A'
    result['price'] = soup.find("li", {"class": "pdp__priceSection__priceListText"}).text.strip() if soup.find("li", {"class": "pdp__priceSection__priceListText"}) else 'N/A'

    return result


def search():
    name = name_entry.get()
    amazon_results = scrape_amazon(name)
    reliance_results = scrape_reliance(name)

    results_text.delete('1.0', tk.END)
    results_text.insert(tk.END, 'AMAZON\n\n')
    for result in amazon_results:
        results_text.insert(tk.END, f"{result['title']}\n{result['price']}\n\n")

    results_text.insert(tk.END, 'RELIANCE DIGITAL\n\n')
    for result in reliance_results:
        results_text.insert(tk.END, f"{result['title']}\n{result['price']}\n\n")


# Create the GUI
root = tk.Tk()
root.title('Product Search')

name_label = tk.Label(root, text='Product Name:')
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

search_button = tk.Button(root, text='Search', command=search)
search_button.pack()

results_text = tk.Text(root)
results_text.pack()

root.mainloop()
