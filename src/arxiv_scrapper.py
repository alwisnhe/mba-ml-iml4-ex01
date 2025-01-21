from bs4 import BeautifulSoup
from dataclass import RawAuthors, RawArticles
from logger import Logger
from requests import get
from utils import get_df_from_model_list
from web_scrapper import WebScrapper, WebScrapperFactory

# --------------------------
# -------DESC: Logger-------
logger = Logger().get_logger()
# --------------------------

# ConcreteProduct
class ArxivScrapperArtigos(WebScrapper):
    def config(self):
        url_base = 'https://arxiv.org/list/cs.AI/recent'

        response = get(url_base)

        response.encoding = 'UTF-8'

        self.soup = BeautifulSoup(response.text, 'html.parser')

    def captar(self) -> None:
        try:
            print(self.soup.title)
            artigosId = self.soup.find(id='articles')
            articles = artigosId.find_all('dt')

            vector_articles = []
            for article in articles:
                title_div = article.find_next('div', class_='list-title')
                span_tag = title_div.find('span', class_='descriptor')
                descriptor = title_div.text.replace(span_tag.text, '').strip()
                pdf_link = article.find('a', id=lambda x: x and x.startswith('pdf-'))['href']
                html_link = article.find('a', id=lambda x: x and x.startswith('html-'))['href'] if article.find('a', id=lambda x: x and x.startswith('html-')) else 'N/A'
                
                vector_articles.append(
                    RawArticles(
                        descricao=descriptor,
                        linkpdf=pdf_link,
                        linkhtml=html_link
                    )
                )
                
            self.df = get_df_from_model_list(models=vector_articles)

        except Exception as e:
            logger.info('-' * 50)
            logger.info(f'Erro: {e}')
            logger.info('-' * 50)

            raise

    def persistir(self) -> None:
        try:
            self.df.to_csv('dados_arxiv_articles.csv')

        except Exception as e:
            logger.info('-' * 50)
            logger.info(f'Erro: {e}')
            logger.info('-' * 50)

            raise


# ConcreteProduct
class ArxivScrapperAutores(WebScrapper):
    def config(self):
        url_base = 'https://arxiv.org/list/cs.AI/recent'

        response = get(url_base)

        response.encoding = 'UTF-8'

        self.soup = BeautifulSoup(response.text, 'html.parser')

    def captar(self) -> None:
        try:
            print(self.soup.title)
            artigosId = self.soup.find(id='articles')
            articles = artigosId.find_all('dt')

            vector_authors = []
            for article in articles:
                title_div = article.find_next('div', class_='list-title')
                span_tag = title_div.find('span', class_='descriptor')
                descriptor = title_div.text.replace(span_tag.text, '').strip()
                authors = [author.text for author in article.find_next('div', class_='list-authors').find_all('a')]
    
                print(f'Descriptor: {descriptor}')
                print(f'Authors: {", ".join(authors)}')
                
                vector_authors.append(
                    RawAuthors(
                        artigos=descriptor,
                        nomes=", ".join(authors)
                    )
                )
                
            self.df = get_df_from_model_list(models=vector_authors)

        except Exception as e:
            logger.info('-' * 50)
            logger.info(f'Erro: {e}')
            logger.info('-' * 50)

            raise

    def persistir(self) -> None:
        try:
            self.df.to_csv('dados_arxiv_authors.csv')
            print('Persistindo autores...')

        except Exception as e:
            logger.info('-' * 50)
            logger.info(f'Erro: {e}')
            logger.info('-' * 50)

            raise

# ConcreteCreator
class ArxivScrapperFactory(WebScrapperFactory):
    def createScrapper(self, *, tipo: str) -> WebScrapper:
        if tipo == 'artigos':
            return ArxivScrapperArtigos()
        elif tipo == 'autores':
            return ArxivScrapperAutores()
        else:
            raise ValueError


if __name__ == '__main__':
    arxiv_scrapper_factory = ArxivScrapperFactory()

    # arxiv_scrapper_artigos = arxiv_scrapper_factory.createScrapper(tipo='artigos')
    # arxiv_scrapper_artigos.config()
    # arxiv_scrapper_artigos.scrapping()

    arxiv_scrapper_autores = arxiv_scrapper_factory.createScrapper(tipo='autores')
    arxiv_scrapper_autores.config()
    arxiv_scrapper_autores.scrapping()
