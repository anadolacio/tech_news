import requests
import time

url = " https://blog.betrybe.com"


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        print(response.status_code)
        time.sleep(1)
        if response.status_code == 200:
            result = response.text
            return result
        else:
            return None
    except requests.exceptions.ReadTimeout:
        return None

    # raise NotImplementedError


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
    raise NotImplementedError
