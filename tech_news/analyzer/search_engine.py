from tech_news.database import search_news
from datetime import datetime


def standardized(query_result):
    return [tuple([result["title"], result["url"]]) for result in query_result]


# Requisito 6
def search_by_title(title):
    formated_title = title.lower()
    search_query = {"title": {"$regex": formated_title}}

    titles_found = search_news(search_query)

    return standardized(titles_found)


# Requisito 7
def search_by_date(date):
    try:
        valid_format = "%Y-%m-%d"
        datetime.strptime(date, valid_format)
    except ValueError:
        raise ValueError("Data inválida")
    else:
        year, month, day = date.split("-")
        db_date_format = f"{day}/{month}/{year}"

        search_query = {"timestamp": db_date_format}
        dates_found = search_news(search_query)

        return standardized(dates_found)


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
