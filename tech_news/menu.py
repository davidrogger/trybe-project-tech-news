import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)


def show_options():
    print(
        "Selecione uma das opções a seguir:"
        "\n 0 - Popular o banco com notícias;"
        "\n 1 - Buscar notícias por título;"
        "\n 2 - Buscar notícias por data;"
        "\n 3 - Buscar notícias por tag;"
        "\n 4 - Buscar notícias por categoria;"
        "\n 5 - Listar top 5 notícias;"
        "\n 6 - Listar top 5 categorias;"
        "\n 7 - Sair.",
        end="",
    )


def end_menu():
    print("Encerrando script\n")


def search_titles():
    inputed = input("Digite o título:")
    titles_found = search_by_title(inputed)
    print(titles_found)


def search_dates():
    inputed = input("Digite a data no formato aaaa-mm-dd:")
    dates_found = search_by_date(inputed)
    print(dates_found)


def search_tags():
    inputed = input("Digite a tag:")
    tags_found = search_by_tag(inputed)
    print(tags_found)


def search_categories():
    inputed = input("Digite a categoria:")
    tags_found = search_by_category(inputed)
    print(tags_found)


def search_top_5_news():
    print(top_5_news())


def search_top_5_categories():
    print(top_5_categories())


def scrape_news():
    inputed = None
    while not isinstance(inputed, int):
        try:
            inputed = int(input("Digite quantas notícias serão buscadas:"))
        except ValueError:
            print("Valor digitado deve ser um número inteiro.")

    news_scrapped = get_tech_news(inputed)
    print(news_scrapped)


# Requisito 12
def analyzer_menu():
    options = {
        "0": scrape_news,
        "1": search_titles,
        "2": search_dates,
        "3": search_tags,
        "4": search_categories,
        "5": search_top_5_news,
        "6": search_top_5_categories,
        "7": end_menu,
    }
    show_options()
    try:
        action = input()
        options[action]()
    except KeyError:
        print("Opção inválida", file=sys.stderr)
