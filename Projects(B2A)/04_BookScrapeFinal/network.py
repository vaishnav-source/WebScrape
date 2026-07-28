import requests
from config import HEADERS

def create_session():
    session = requests.Session()
    session.headers.update(HEADERS)
    return session