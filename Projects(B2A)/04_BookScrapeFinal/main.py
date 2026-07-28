from database import (
    connect_database,
    create_table,
    upsert_book
)

from config import PAGE_URL, HEADERS
from logger import logger
from scraper import  scrape_book
import requests
from failed_manager import (get_failed_urls, replace_failed_urls, save_failed_urls)
from url_collector import collect_product_urls
from progress_manager import ProgressManager


conn, cursor = connect_database()

session = create_session()
session.headers.update(HEADERS)

product_urls = collect_product_urls(session)
logger.info(f"Collected {len(product_urls)} product URLs.")


try:
    logger.info("Scrape Started")
    create_table(cursor)
    total_books = 0
    progress = ProgressManager(len(product_urls))
    for product_url in product_urls:
        logger.info(f"Scraping book {product_url}")
        book_data = scrape_book(session, product_url)
        

        if book_data:
            upsert_book(cursor, book_data)
            total_books += 1
        progress.update()
        progress.display()
    conn.commit()
    failed_urls = get_failed_urls()
    if failed_urls:
        logger.info(f"Retrying {len(failed_urls)} failed books...")
        replace_failed_urls([])
        for url in failed_urls:
            book_data = scrape_book(session, url)
            if book_data:
                upsert_book(cursor, book_data)
            
        conn.commit()
        
        if get_failed_urls():
            logger.warning(f"{len(get_failed_urls())} books still failed.")
            save_failed_urls()
        else:
            logger.info("All failed books were recovered successfully.")
    
    logger.info(f"Scrape completed - Books: {total_books}")
    print(f"Total books processed: {total_books}")

except Exception as error:
    logger.exception(f"Program failed: {error}")
    conn.rollback()

finally:
    session.close()
    conn.close()