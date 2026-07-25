import time
import requests

from bs4 import BeautifulSoup

from config import (
    BASE_URL,
    HEADERS,
    TIMEOUT,
    REQUEST_DELAY
)

from logger import logger

from database import (
    connect_database,
    create_table,
    insert_book,
    get_all_books,
    close_connection
)


def scrape_books(page):
    books_data=[]
    url = BASE_URL.format(page)
    try:
        logger.info(f"Scraping page {page}")
        response = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        books = soup.find_all('article',class_="product_pod")
        for book in books:
            title = book.find("h3").find("a").get("title")
            price_text = book.find("p",class_="price_color").text
            price = float("".join(ch for ch in price_text if ch.isdigit() or ch =="."))
            stock = book.find("p",class_="instock availability").text.strip()
            rating = book.find("p",class_="star-rating")["class"][1]
            book_data ={
                "title" : title,
                "price" : price,
                "stock" : stock,
                "rating" : rating
                    }
            books_data.append(book_data)
        return(books_data)
    except requests.RequestException as error:
        logger.error(f"Failed to scrape page {page}: {error}")
        raise

