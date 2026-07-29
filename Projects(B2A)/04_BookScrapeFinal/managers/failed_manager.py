import os
from config import FAILED_URL_FILE
failed_urls =[]

def add_failed_urls(url):
    failed_urls.append(url)

def get_failed_urls(url):
    return failed_urls

def replace_failed_urls(new_urls):
    failed_urls.clear()
    failed_urls.extend(new_urls)


def save_failed_urls(url):
    os.makedirs(os.path.dirname(FAILED_URL_FILE), exist_ok=True)
    with open (FAILED_URL_FILE,"w") as file:
        for url in  failed_urls:
            file.write(url+"\n")