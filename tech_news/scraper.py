from parsel import Selector
import requests
import time
from tech_news.database import create_news

url = "https://blog.betrybe.com"


# Requisito 1
def fetch(url):
    """Seu código deve vir aqui"""
    try:
        response = requests.get(url, timeout=3)
        # print(response.status_code)
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
    # raise NotImplementedError
    try:
        selector = Selector(text=html_content)
        result = selector.css(".entry-title a::attr(href)").getall()
        return result
    except Exception:
        return []


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""
    # raise NotImplementedError
    try:
        selector = Selector(text=html_content)
        result = selector.css(".next::attr(href)").get()
        return result
    except Exception:
        return None


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""
    # raise NotImplementedError
    result_dic = Selector(html_content)
    url = result_dic.css("link[rel=canonical]::attr(href)").get()
    title = result_dic.css(".entry-title::text").get().strip()  # type: ignore
    timestamp = result_dic.css(".meta-date::text").re_first(
        r"\d{2}/\d{2}/\d{4}"
    )
    writer = result_dic.css(".author a::text").get()
    reading_time = result_dic.css(".meta-reading-time::text").re_first(r"\d+")
    summary = result_dic.css(
        ".entry-content > p:first-of-type *::text"
    ).getall()
    category = result_dic.css(".category-style .label::text").get()

    result = {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),  # type: ignore
        "summary": "".join(summary).strip(),
        "category": category,
    }
    return result


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com"
    """Seu código deve vir aqui"""
    # raise NotImplementedError
    all_news = []

    while len(all_news) < amount:
        html_content = fetch(url)
        all_news.extend(scrape_updates(html_content))
        url = scrape_next_page_link(html_content)

    news = all_news[:amount]
    news_itens = []
    for new in news:
        fetch_ = fetch(new)
        scrape_ = scrape_news(fetch_)
        news_itens.append(scrape_)
    all_news = news_itens

    create_news(all_news)

    return all_news
