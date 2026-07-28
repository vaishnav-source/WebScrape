import requests
from config import HEADERS,PAGE_URL,TIMEOUT
from urllib.parse import urljoin

from bs4 import BeautifulSoup



def collect_product_urls(session):
    product_urls = []
    seen_urls = set()
    page_url = PAGE_URL.format(1)
    while page_url:
        response = session.get(page_url,
            timeout = TIMEOUT)
        response.raise_for_status()
        soup = BeautifulSoup(response.text,'html.parser')
        books = soup.find_all('article',class_="product_pod")
        for book in books:
            book_link = book.find("h3").find("a")
            book_relative_url = book_link["href"]
            product_url = urljoin(page_url,book_relative_url)
            if product_url not in seen_urls:
                seen_urls.add(product_url)
                product_urls.append(product_url)
        next_button = soup.find("li",class_="next")
        if next_button:
            next_relative_url = next_button.find("a",href=True)["href"]
            page_url = urljoin(page_url,next_relative_url)
        else:
            page_url = None
    return product_urls

   
    
