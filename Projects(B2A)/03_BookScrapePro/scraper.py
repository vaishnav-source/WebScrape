import requests
import time
from bs4 import BeautifulSoup
from config import HEADERS,TIMEOUT,REQUEST_DELAY
from urllib.parse import urljoin

RATING_MAP = {
    "One" : 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
def scrape_book(product_url):
    response = requests.get(
        product_url,
        headers=HEADERS,
        timeout=TIMEOUT
    )
    if response.status_code !=200:
        raise Exception(f"Failed to load pages :{product_url}")
    
    response.encoding = response.apparent_encoding
    
    soup = BeautifulSoup(response.text,"html.parser")
    book = soup.find("article",class_="product_page")
    title = book.find("h1").get_text(strip=True)
    price_text = book.find("p",class_="price_color").text
    price =float("".join(ch for ch in price_text if ch.isdigit() or ch =="."))
    availability = book.find("p",class_="instock availability").get_text(strip=True)
    rating =RATING_MAP[book.find("p",class_="star-rating")["class"][1]] 
    description_section = book.find("div", id="product_description")
    if description_section:
        description = description_section.find_next_sibling("p").get_text(strip=True)
    else:
        description = ""
    breadcrumb  =soup.find("ul",class_="breadcrumb")
    category = breadcrumb.find_all("li")[2].get_text(strip=True)
    return {
        "product_name": title,
        "product_url": product_url,
        "price" : price,
        "rating" : rating,
        "description":description,
        "availability": availability,
        "category" : category

    }

def scrape_page(page_url):
    response =requests.get(
        page_url,
        headers=HEADERS,
        timeout=TIMEOUT
    )

    if response.status_code !=200:
        raise Exception (f"Failed to load page: {page_url}")
    soup = BeautifulSoup(response.text,'html.parser')
    books = soup.find_all('article',class_="product_pod")
    all_books=[]
    for book in books:
        relative_url = book.find("a")["href"]
        product_url = urljoin(page_url, relative_url)
        book_data = scrape_book(product_url)
        all_books.append(book_data)
        time.sleep(REQUEST_DELAY)
    next_button = soup.find("li",class_="next")
    if next_button:
        next_relative_url  = next_button.find("a")["href"]
        next_page_url = urljoin(page_url,next_relative_url)
    else:
          next_page_url = None

    return all_books, next_page_url
