from tech_news.database import get_collection
from tech_news.analyzer.search_engine import standardized


# Requisito 10
def top_5_news():
    first_criterion = "comments_count"
    second_criterion = "title"
    descending_order = -1
    ascending_order = 1

    db = get_collection()

    news_found = (
        db.find()
        .sort(
            [
                (first_criterion, descending_order),
                (second_criterion, ascending_order),
            ]
        )
        .limit(5)
    )

    return standardized(news_found)


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
