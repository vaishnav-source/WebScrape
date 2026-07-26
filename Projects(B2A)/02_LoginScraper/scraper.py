from bs4 import BeautifulSoup
from config import (SECURE_PAGE_URL,HEADERS,TIMEOUT)

def scrape_secure_page(session):
    secure_page_response =session.get(SECURE_PAGE_URL,
                                      headers=HEADERS,
                                      timeout = TIMEOUT)
    if secure_page_response.status_code !=200:
        raise Exception("Failed to access secure page")
    soup =BeautifulSoup(secure_page_response.text,"html.parser")
    heading = soup.find("h2").get_text(strip=True)
    message = soup.find("h4").get_text(strip=True)
    return{"heading":heading,
           "message":message}
