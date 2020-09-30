'''
############## COLETA DE DADOS ##############

O site foi desenvolvido em uma estrutura bem simples, não utilizando javascript ou iframes em sua navegação. 
Isto nos permite utilizar bibliotecas mais simples de requisição, como o próprio BS4 ao invés de uma biblioteca 
mais interativa com o navegador, como o Selenium. 

O site possui url's amigáveis em relação as páginas onde podemos obter os links dos livros, por exemplo, para a página 1 basta acessar a url:
- http://books.toscrape.com/catalogue/category/books_1/page-1.html
Caso seja a página 2: 
- http://books.toscrape.com/catalogue/category/books_1/page-2.html

Ou seja, podemos navegar através da páginas com um loop por exemplo.

Para tornar o processo de crawling mais rápido, será utilizado programação paralela (threads). Portanto, para
melhor controle do que estaremos executando, em quais páginas, utilizarei uma programação baseada em classes e funções
de getters e setters
'''

# importação das bibliotecas
import time
import requests
import threading
import pandas as pd

from pathlib import Path
from word2number import w2n
from bs4 import BeautifulSoup
from datetime import datetime as dt

# criando as variaveis globais
# numero maximo de workers que queremos que façam a tarefa de crawling simultaneamente
# um numero alto pode afetar o processamento/memória
n_max_workers = 5

# definindo o limite máximo de threads simultaneas
# a biblioteca de threading já inicia com algumas threads ativas para controle
# então o nosso número de threads totais deverá ser as threads defaults + o nosso limite de workers
active_threads = threading.active_count() + n_max_workers

# definindo a nossa classe de controle
class Crawler_controller():
    def __init__(self):
        # definindo a variável em que armazenaremos a url de cada livro por cada página.
        # cada key do dicionário será a url da página, e o valor será uma lista
        # com todos os livros que contém na página
        self._pages_urls = {}
        
        # instancia uma variável que será o controle das urls já visitadas
        self._visited_urls = []
        
        # armazena os dados das páginas dos livros crawlados
        self._books_crawled = []
        
        # armazena o numero da página que deve ser crawlada pelo worker
        self._page_number = 1
        
        self._page_404 = 0
        
    # se acessarmos uma url, adicionaremos ela para não visita-la novamente
    def add_visited_url(self, url):
        if url not in self._visited_urls:
            self._visited_urls.append(url)
    
    # verifica se a url já foi visitada
    # return: True or False
    def is_a_visited_url(self, url):
        if url in self._visited_urls:
            return True
        else:
            return False

    # obtem uma URL com página incremental toda vez que a função for chamada
    def get_page_url(self):
        page_number = self._page_number
        self._page_number += 1
        return f'http://books.toscrape.com/catalogue/category/books_1/page-{page_number}.html'
    
    # caso a página não exista, o erro 404 será retornado
    # a intenção é ter um controle para saber quando parar as threads
    def increment_404_pages_url(self):
        self._page_404 += 1

    # após 6 páginas ocorrendo erro 404 as threads serão terminadas        
    def stop_404_pages(self):
        if self._page_404 > 6:
            return True
        return False
    
    # função para adicionar a url de cada livro para visitarmos depois
    def add_urls_to_crawl(self, url_page, url_list):
        # verifica se a página já existe no dicionário, se não existir, iremos criar e adicionar a url dos livros
        if url_page not in self._pages_urls:
            self._pages_urls[url_page] = url_list
            # adiciona a url da pagina a lista de urls visitados
            self.add_visited_url(url_page)
        
    # obtem as informações dos livros das páginas que foram crawladas  para dentro da variavel da classe
    def add_book_crawled(self, book_info):
        self._books_crawled.append(book_info)
        # adiciona a url do livro a lista de urls visitados
        self.add_visited_url(book_info['url'])
    
    # retorna uma lista de urls dos livros para o worker crawlar que foram obtidas a partir do crawling das páginas
    # return: a url da página e a lista de urls de livros daquela página
    # se não existir mais páginas para crawlar, retornará False para terminar a thread
    def get_urls_to_crawl(self):
        if crawler_controller._pages_urls.keys():
            url = list(crawler_controller._pages_urls.keys())[0]
            books_url = crawler_controller._pages_urls[url]
            del crawler_controller._pages_urls[url]
            print('--> Working on: {url}')
            return [url, books_url]
        return [False, False]
    
    # exporta os dados que foram crawlados para um arquivo csv
    def exports_to_file(self, file_path):
        data_export = pd.DataFrame(self._books_crawled)
        data_export.to_csv(file_path, sep=';', index=False, encoding='iso-8859-1')

# função que será responsável por obter a url dos livros em cada página
# url base das paginas que contem a lista de livros
base_url = 'http://books.toscrape.com/catalogue/'
def get_books_url_from_page():
    try:
        # busca a url de qual página deverá ser consultada
        # a função get_page_url já faz um incremento de página toda vez que é executada
        url_request = crawler_controller.get_page_url()
        page = requests.get(url_request)
        status_code = int(page.status_code)
    except:
        status_code = 404

    if status_code != 404:
        soup = BeautifulSoup(page.text, 'html.parser')

        # obtem a div que contém todos os livros
        books_in_page = soup.select("#default > div > div > div > div > section > div:nth-child(2)")[0]
        # dentro da div, busca todos os links
        books_urls_in_page = books_in_page.findAll('a')
        # aplicando algumas correções para se tornar uma uri para o crawler 
        # conseguir realizar o request
        books_urls_to_crawl = []
        for book_link in books_urls_in_page:
            href = book_link['href'].replace('../../', base_url)
            if ('http://' in href or 'https://' in href) and href not in books_urls_to_crawl:
                books_urls_to_crawl.append(href)

        # adiciona a url para dentro da nossa classe
        crawler_controller.add_urls_to_crawl(url_request, books_urls_to_crawl)
    else:
        crawler_controller.increment_404_pages_url()


# função responsável por obter os dados dos livros em cada url de livro acessada
def get_book_info(book_url):
    page = requests.get(book_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    # obtem os dados com selector
    title = soup.select('#default > div > div > ul > li.active')[0].text.strip()
    category = soup.select('#default > div > div > ul > li:nth-child(3)')[0].text.strip()
    
    # obtem a qtd de estrelas, a qtd de estrelas é um atributo de classe dentro da tag p
    star_rating = soup.select('#content_inner > article > div.row > div.col-sm-6.product_main > p.star-rating')[0]
    star_rating['class'].remove('star-rating')
    stars = 0
    for e in star_rating['class']:
        try:
            # converte a classe string para inteiro (Three --> 3, Two --> 2)
            stars = w2n.word_to_num(e.strip())
        except:
            pass   
    # obtem os dados da tabela que tem o preço e a qtd em estoque
    table_data = pd.read_html(str(soup.find('table')))[0]
    price = table_data.iloc[2, 1]
    in_stock = table_data.iloc[5, 1]

    return {
        'url': book_url,
        'title': title,
        'category': category,
        'stars': stars,
        'price': price,
        'in_stock': in_stock
    }

'''
Worker responsável por executar a função --> get_books_url_from_page
Que irá solicitar uma URL de uma página que contem uma lista de livros,
obter a lista de todos os links que dão acesso ao informações do livro e
adicionar os links para dentro da nossa classe de controle, que a partir daí,
outro worker irá acessar cada URL e pegar as informações que queremos
'''
def start_workers_pages_url():
    # while infinito até atingir a qtd de páginas 404
    while not crawler_controller.stop_404_pages():
        # limita a criação do numero de threads
        if threading.active_count() < active_threads:
            # cria e starta a nossa thread (worker) executando a função get_books_url_from_page
            worker = threading.Thread(target=get_books_url_from_page)
            worker.start()
        else:
            time.sleep(5)


'''
A única funcionalidade desta função é acessar a lista de urls dos livros de
de cada página que obtemos anteriormente e pegar as informações que queremos
Criamos ela separada por conta que será utilizado um for e estará executando 2 tarefas
a de obter os dados e a de gravar os dados na classe de controle (assim a solução fica mais
modularizada se houver necessidade de manutenção por conta de mudança na estrutura do site)
'''
def get_books_info_from_urls(urls):
    for url in urls:
        # verifica se a url não foi visitada
        if not crawler_controller.is_a_visited_url(url):
            book_info = get_book_info(url)
            crawler_controller.add_book_crawled(book_info)

# Worker para obter os dados dos livros
# Cada worker irá obter uma lista de urls das páginas que 
# que consultamos a listagem dos livros através da função get_urls_to_crawl
def start_workers_books_url():
    # cria um loop infinito até que não tenha mais nenhuma URL de livro para consultar
    work_done = False
    while not work_done:
        # limita a criação do numero de threads
        if threading.active_count() < active_threads:
            # obtem a lista de url de livros e a url da página em que a lista de urls foi retirada
            # que utilizaremos para dar nome a nossa thread (worker)
            th_name, urls_to_crawl = crawler_controller.get_urls_to_crawl()
            # se existir url para consultar (se a lista não é vazia ou o valor é falso)
            if urls_to_crawl:
                # cria e starta nosso worker passando a lista de urls de livros a ser consultada
                worker = threading.Thread(target=get_books_info_from_urls, args=(urls_to_crawl,), name=th_name)
                worker.start()
            else:
                # se não existir mais urls para buscar, então encerra o loop
                work_done = True
        else:
            time.sleep(5)

if __name__ == '__main__':
    # Iniciando a nossa classe de controle
    crawler_controller = Crawler_controller()

    # starta os workers para começarem a buscar a lista de livros nas páginas
    start_workers_pages_url()

    # starta os workers para começaram a buscar as informações dos livros
    # a partir da lista de urls que obtivemos com os workers acima
    start_workers_books_url()

    # exporta os dados obtidos para um arquivo csv
    prefix = dt.now().strftime('%Y-%m-%d--%H_%M_%S')
    file_name = Path(f'./data/pending-{prefix}-crawl-data.csv')
    crawler_controller.exports_to_file(file_name)