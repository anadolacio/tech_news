from tech_news.database import find_news


# Requisito 7
def search_by_title(title):
    """Seu código deve vir aqui"""
    # raise NotImplementedError
    data = find_news()

    news_title = []

    for new in data:
        if title.lower() in new["title"].lower():
            result = (new["title"], new["url"])
            news_title.append(result)

    return news_title


# Requisito 8
def search_by_date(date):
    """Seu código deve vir aqui"""
    raise NotImplementedError


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
    # raise NotImplementedError
    data = find_news()

    news_category = []

    for new in data:
        if category.lower() in new["category"].lower():
            result = (new["title"], new["url"])
            news_category.append(result)

    return news_category
