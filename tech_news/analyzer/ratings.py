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
    db = get_collection()

    pipeline = [
        {"$group": {"_id": "$category", "count": {"$sum": 1}}},
        {"$sort": {"count": -1, "_id": 1}},
    ]

    counted_categotires = list(db.aggregate(pipeline))
    categories = [category["_id"] for category in counted_categotires[:5]]

    return categories
