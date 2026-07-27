from database import (
    connect_database,
    create_table,
    upsert_book
)

from config import PAGE_URL
from logger import logger
from scraper import scrape_page


conn, cursor = connect_database()

try:
    logger.info("Scrape Started")
    create_table(cursor)

    page_url = PAGE_URL.format(1)
    total_pages = 0
    total_books = 0

    while page_url:
        logger.info(f"Scraping page: {page_url}")
        books, next_page_url = scrape_page(page_url)
        total_pages += 1
        total_books += len(books)

        for book in books:
            upsert_book(cursor, book)

        page_url = next_page_url
        

    conn.commit()
    logger.info(
    f"Scrape completed - Pages: {total_pages}, Books: {total_books}"
    )

    print(f"Total pages scraped: {total_pages}")
    print(f"Total books processed: {total_books}")

except Exception as error:
    print(f"Program failed: {error}")
    conn.rollback()

finally:
    conn.close()