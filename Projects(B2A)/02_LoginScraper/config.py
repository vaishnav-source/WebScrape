# Website ConfigurationB
BASE_URL = "https://the-internet.herokuapp.com"

LOGIN_PAGE_URL = "https://the-internet.herokuapp.com/login"

LOGIN_POST_URL = "https://the-internet.herokuapp.com/authenticate"

SECURE_PAGE_URL = "https://the-internet.herokuapp.com/secure"

# Request Configuration
HEADERS ={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36"

}

TIMEOUT = 10    

REQUEST_DELAY = 2
# Logger
LOG_FILE = "logs/scraper.log"
LOG_LEVEL = "INFO"
# Database
DATABASE_NAME = "login.db"