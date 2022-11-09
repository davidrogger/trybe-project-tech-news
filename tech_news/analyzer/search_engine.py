from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    formated_title = title.lower()
    search_query = {"title": {"$regex": formated_title}}

    titles_found = [
        tuple([result["title"], result["url"]])
        for result in search_news(search_query)
    ]

    return titles_found


# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
