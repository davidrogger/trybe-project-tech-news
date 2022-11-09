# Sobre o Projeto 

- Terceiro projeto do modulo de Ciências da Computação da trybe.
- Raspagem de dados tema da seção 3, que aborda, o conceito e abordagem de coleta de dados pela web, apresentando ferramentas conhecidas como, [Requests](https://requests.readthedocs.io/en/latest/), [Parsel](https://parsel.readthedocs.io/en/latest/usage.html), [Selenium](https://www.selenium.dev/), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) e uso do [pymongo](https://pymongo.readthedocs.io/en/stable/) para salvar as informações coletadas em um mango de dados mongodb.
- Desenvolvido metodos, para requisitar e coletar dados do [blog da trybe](https://blog.betrybe.com/) e salvar no banco mongodb.

<details>
  <summary>
    <strong>
      :telescope: Usando menu interativo CLI:
    </strong>
  </summary>

Em construção...

</details>

#

# Tecnologias e ferramentas usadas 🛠

![Python](https://img.shields.io/badge/-Python-%23F7DF1C?style=flat-square&logo=python)
![Docker](https://img.shields.io/badge/-Docker-003f8c?style=flat-square&logo=docker&logoColor=fff)


# Desafios

- Maior desafio foi de lidar com "subtags" quando coletando algum tag especifico, se ele possuia uma tag dentro dele, como um negrito ou itálico, usando o parsel, usando o filtro para coleta somente do texto, ele acaba que ignora alguns elementos, depois de muita pesquisa, e tentativa de entender como usar melhor os seletores css, para coleta, foi possivel coletar o primeiro paragrafo de cada noticia juntamente com suas tags filhas.

# Conclusão

- Muito gratificante a conclusão de mais um projeto onde aprendi muito com apenas 11 requisitos.

# Iniciando o Projeto Tech News.

Importante: seguir a ordem apresentada a baixo, para o funcionamento.

<details>
  <summary>
    <strong>
      ⚠️ Configurações mínimas para execução do projeto
    </strong>
  </summary>

   - Sistema Operacional Distribuição Unix
 - Python versão >= 3.8.10 

</details>

<details>
  <summary>
    <strong>
      ⚠️ Inicie o docker-compose
    </strong>
  </summary>

Para ver a aplicação funcionando basta iniciar o docker compose, basta esta na pasta do repositório tendo o requisitos conforme informado na aba de requisitos, e iniciar o docker com `docker-compose up -d`

Após levantar o container para interagir com os comandos de linha, é necessário acessar o container usando o comando a seguir, `docker exec -it tech_news bash`, dentro do terminal do container é necessário entrar no ambiente virtual do python com o comando, `source .venv/bin/activate`, após esse comando o inicio do terminal deve aparecer com `(.venv)` antes do root, deve-se usar o comando `pip install .` para instalar o menu, após isso basta usar o comando apresentado na parte de amostra.



</details>

</details>

<details>
  <summary>
    <strong>
      :newspaper_roll: Requisitos solicitados durante o desenvolvimento do projeto
    </strong>
  </summary>

 
### Resultado por requisito
*Nome* | *Avaliação*
--- | :---:
1 - Crie a função fetch | :heavy_check_mark:
2 - Crie a função scrape_novidades | :heavy_check_mark:
3 - Crie a função scrape_next_page_link | :heavy_check_mark:
4 - Crie a função scrape_noticia | :heavy_check_mark:
5 - Crie a função get_tech_news para obter as notícias! | :heavy_check_mark:
6 - Crie a função search_by_title | :heavy_check_mark:
7 - crie a função search_by_date | :heavy_check_mark:
8 - Crie a função search_by_tag | :heavy_check_mark:
9 - Crie a função search_by_category | :heavy_check_mark:
10 - Crie a função top_5_news | :heavy_check_mark:
11 - Crie a função top_5_categories | :heavy_check_mark:
12 - Crie a função analyzer_menu | :heavy_check_mark:
13 - Implemente as funcionalidades do menu | :heavy_check_mark:


</details>
