import requests
import os 
from dotenv import load_dotenv
from config import(LOGIN_PAGE_URL,LOGIN_POST_URL,SECURE_PAGE_URL,HEADERS,TIMEOUT)


load_dotenv()
USERNAME = os.getenv("LOGIN_USERNAME")
PASSWORD =os.getenv("LOGIN_PASSWORD")

def login():
    session =requests.Session()
    login_page_response =session.get(LOGIN_PAGE_URL, 
                                     headers =HEADERS,
    timeout = TIMEOUT)
    
    if login_page_response.status_code != 200:
        raise Exception("Failed to load login page.")
    
    login_response = session.post(LOGIN_POST_URL,
                                 data = {
                                 "username": USERNAME,
                                  "password" : PASSWORD
                                  },
    headers =HEADERS,
    timeout = TIMEOUT
    )
    if login_response.url != SECURE_PAGE_URL:
        raise Exception("Login Failed")
    
    return session