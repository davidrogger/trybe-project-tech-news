import requests
import time
from parsel import Selector
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    try:
        response = requests.get(url, headers=headers, timeout=3)
        response.raise_for_status()
        time.sleep(1)
    except (requests.HTTPError, requests.ReadTimeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(html_content)
    news_links = selector.css(".entry-title a::attr(href)").getall()
    return news_links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    next_page_link = selector.css(".next::attr(href)").get()
    return next_page_link


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(html_content)

    url = selector.css("head link[rel='canonical']::attr(href)").get()
    title = selector.css(".entry-title::text").get().strip()
    timestamp = selector.css(".meta-date::text").re_first(r"\d{2}/\d{2}/\d{4}")
    writer = selector.css(".author a::text").get()
    comments_count = int(
        selector.css(".post-comments .title-block::text").re_first(r"\d")
        or "0"
    )

    raw_summary = selector.css(
        ".entry-content > p:first-of-type *::text"
    ).getall()

    summary = "".join(raw_summary).strip()

    tags = selector.css(".post-tags a::text").getall()
    category = selector.css(".category-style .label::text").get()

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary,
        "tags": tags,
        "category": category,
    }


def get_last_n_news_links(n):
    url = "https://blog.betrybe.com/"
    news_links = []
    while len(news_links) < n:
        html = fetch(url)
        news_links.extend(scrape_novidades(html))
        url = scrape_next_page_link(html)

    return news_links[:n]


# Requisito 5
def get_tech_news(amount):
    news_links = get_last_n_news_links(amount)
    news_infos = []

    for news_link in news_links:
        html = fetch(news_link)
        news_info = scrape_noticia(html)
        news_infos.append(news_info)

    create_news(news_infos)

    return news_infos
