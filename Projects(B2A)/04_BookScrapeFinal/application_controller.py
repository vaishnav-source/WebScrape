from url_collector import collect_product_urls
from scrapers.scraper_factory import ScraperFactory
from database import connect_database,create_table,upsert_book
from repositories.book_repository import BookRepository
from managers.failed_manager import get_failed_urls,replace_failed_urls,save_failed_urls
from managers.progress_manager import ProgressManager
from config import HEADERS
from network import create_session
from logger import logger

class ApplicationController:
    def __init__(self):
        self.conn , self.cursor = connect_database()
        self.session = create_session()
        self.session.headers.update(HEADERS)
        self.scraper = ScraperFactory.get_scraper()
        self.book_repository = BookRepository(self.conn)

    def run(self):
        try:
            self.prepare_database()
            self.collect_urls()
            self.process_urls()
        finally:
             self.cleanup()

    def collect_urls(self):
        self.product_urls = collect_product_urls(self.session)
        logger.info(
            f"Collected {len(self.product_urls)} product URLs."
        )
        self.progress = ProgressManager(len(self.product_urls))

    def prepare_database(self):
        create_table(self.cursor)

    def process_urls(self):
        total_books = 0
        for product_url in self.product_urls:
                book_data = self.process_single_book(product_url)
                
        
                if book_data:
                    self.book_repository.save(book_data)
                    total_books += 1
                self.progress.update()
                self.progress.display()
        
        self.retry_failed_urls()
        logger.info(f"Successfully scraped {total_books} books.")


    def process_single_book(self,product_url):
        logger.info(f"Scraping book {product_url}")
        book_data = self.scraper.scrape_book(self.session,product_url)
        return book_data

    def retry_failed_urls(self):
        failed_urls = get_failed_urls()
        if failed_urls:
                logger.info(f"Retrying {len(failed_urls)} failed books...")
                replace_failed_urls([])
                for url in failed_urls:
                    book_data = self.process_single_book(url)
                    if book_data:
                        upsert_book(self.cursor, book_data)
                    
                self.conn.commit()
                remaining_failed = get_failed_urls()
                if remaining_failed :
                    logger.warning(f"{len(remaining_failed)} books still failed.")
                    save_failed_urls()
                else:
                    logger.info("All failed books were recovered successfully.")

    def  cleanup(self):
         logger.info("Cleaning up resources")   
         self.session.close()   
         self.conn.close()
         logger.info("Cleanup completed ")
