BASE_URL = "https://books.toscrape.com"
PAGE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
HEADERS ={
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"
}
TIMEOUT = 10
REQUEST_DELAY = 0.5
DATABASE_NAME = "books.db"
LOG_FILE = "logs/Scraper.log"
LOG_LEVEL = "INFO"
MAX_RETRIES = 3
RETRY_DELAY = 2
FAILED_URL_FILE = "failed/failed_books.txt"