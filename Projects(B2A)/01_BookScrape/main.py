import time
from scraper import scrape_books
from logger import logger
from database import ( connect_database ,  create_table , insert_book  ,get_all_books ,close_connection)
from config import REQUEST_DELAY

conn, cursor = connect_database()

try:
    logger.info("Scraper started")
    create_table(cursor)

    for page in range(1, 51):
         
         books = scrape_books(page)

         for book in books:
               insert_book(cursor, book)
               print(book)

         time.sleep(REQUEST_DELAY)

    conn.commit()
    logger.info("Scraping completed successfully")

except Exception as error:
    conn.rollback()
    logger.error(f"Program failed: {error}")

finally:
    conn.close()
    logger.info("Database connection closed")