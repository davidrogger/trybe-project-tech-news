import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)

GREEN = "\033[32m"
BLUE = "\033[36m"
RED = "\033[31m"
END = "\033[0m"


def standard_print(data):
    title = " RESULTADOS "
    print(f"\n{title:#^40}")
    if len(data) == 0:
        print(f"{RED}Nenhum dado foi encontrado.{END}\n")
    for title in data:
        print(f"\nTitle: {title[0]}" f"\nURL: {title[1]}\n")


def show_options():
    title = " MENU "
    print(f"\n{title:#^40}")
    print(
        f"{BLUE}Selecione uma das opções a seguir:{END}"
        "\n 0 - Popular o banco com notícias;"
        "\n 1 - Buscar notícias por título;"
        "\n 2 - Buscar notícias por data;"
        "\n 3 - Buscar notícias por tag;"
        "\n 4 - Buscar notícias por categoria;"
        "\n 5 - Listar top 5 notícias;"
        "\n 6 - Listar top 5 categorias;"
        "\n 7 - Sair."
        "\n"
    )


def end_menu():
    print(f"\n{BLUE}Encerrando script{END}\n")


def search_titles():
    inputed = input("\nDigite o título: ")
    titles_found = search_by_title(inputed)
    standard_print(titles_found)


def search_dates():
    inputed = input("Digite a data no formato aaaa-mm-dd: ")
    dates_found = search_by_date(inputed)
    standard_print(dates_found)


def search_tags():
    inputed = input("Digite a tag: ")
    tags_found = search_by_tag(inputed)
    standard_print(tags_found)


def search_categories():
    inputed = input("Digite a categoria: ")
    tags_found = search_by_category(inputed)
    standard_print(tags_found)


def search_top_5_news():
    news_found = top_5_news()
    standard_print(news_found)


def search_top_5_categories():
    categories_found = top_5_categories()
    for position, category in enumerate(categories_found, start=1):
        print(f"{position} - {category}")


def scrape_news():
    inputed = None
    while not isinstance(inputed, int):
        try:
            inputed = int(input("Digite quantas notícias serão buscadas: "))
        except ValueError:
            print("Valor digitado deve ser um número inteiro.")

    print("Aguarde alguns segundos enquanto os dados são coletados e salvos.")
    get_tech_news(inputed)


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
    action = "inicializando"
    while action != "7":
        try:
            show_options()
            action = input(f"{GREEN}Digite uma das opções:{END} ")
            options[action]()
        except KeyError:
            print(f"{RED}\nOpção inválida{END}\n", file=sys.stderr)
        except ValueError:
            print(
                f"{RED}\nDeve seguir um formato de data válido{END}\n",
                file=sys.stderr,
            )
