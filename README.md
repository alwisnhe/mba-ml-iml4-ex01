# iml4-exemplo-atividade1

Exercício da atividade 1 de IML4

## Menu

- [Estrutura do Projeto](#estrutura-do-projeto)
- [Explicação do Projeto](#explicação-do-projeto)
- [Bibliotecas Utilizadas](#bibliotecas-utilizadas)
- [Como Executar](#como-executar)
- [Versão](#versão)

## Estrutura do Projeto

A estrutura do projeto é organizada da seguinte forma:


### Descrição dos Arquivos e Diretórios

- `.bumpversion.cfg`: Configuração para o gerenciamento de versões do projeto.
- `.gitignore`: Arquivo que especifica quais arquivos e diretórios devem ser ignorados pelo Git.
- `.pre-commit-config.yaml`: Configuração para os hooks de pré-commit.
- `dados_arxiv_articles.csv`: Arquivo CSV contendo os dados dos artigos coletados do arXiv.
- `dados_arxiv_authors.csv`: Arquivo CSV contendo os dados dos autores coletados do arXiv.
- `Makefile`: Arquivo que define comandos para automatizar tarefas do projeto.
- `poetry.lock`: Arquivo de bloqueio de dependências gerado pelo Poetry.
- `pyproject.toml`: Arquivo de configuração do Poetry para o gerenciamento de dependências e pacotes.
- `README.md`: Arquivo que contém a documentação do projeto.

### Diretório `src/`

- `arxiv_scrapper.py`: Script principal para coletar dados do arXiv. Este script utiliza as funções definidas nos outros arquivos para realizar o scraping e armazenar os dados.
- `dataclass.py`: Define classes de dados utilizadas no projeto para representar artigos e autores.
- `logger.py`: Configura e gerencia o sistema de logging, permitindo registrar logs das operações realizadas pelo scrapper.
- `singleton.py`: Implementa o padrão de design Singleton para garantir que certas classes tenham apenas uma única instância.
- `utils.py`: Contém funções utilitárias usadas em todo o projeto, como funções auxiliares para manipulação de dados.
- `web_scrapper.py`: Contém funções específicas para realizar o scraping da web, como funções para fazer requisições HTTP e parsear o HTML retornado.

## Explicação do Projeto

Este projeto é um scrapper para coletar dados do arXiv, um repositório de artigos científicos. O projeto inclui scripts para extrair informações de artigos e autores do arXiv e armazená-las em arquivos CSV. Além disso, o projeto utiliza padrões de design como Singleton e Logger para garantir uma arquitetura de código limpa e eficiente.

## Bibliotecas Utilizadas

- `requests`: Para fazer requisições HTTP ao site do arXiv.
- `beautifulsoup4`: Para fazer o parsing do HTML retornado pelo arXiv.
- `pandas`: Para manipulação e armazenamento dos dados em formato CSV.
- `dataclasses`: Para definir classes de dados de forma simples e eficiente.
- `logging`: Para registrar logs das operações realizadas pelo scrapper.
- `singleton_decorator`: Para implementar o padrão de design Singleton.
- `pytest`: Para testes unitários.
- `pre-commit`: Para gerenciamento de hooks de pré-commit.
- `bumpversion`: Para gerenciamento de versões do projeto.
- `poetry`: Para gerenciamento de dependências e pacotes.

## Como Executar

1. Instale as dependências do projeto utilizando o Poetry:
    ```sh
    poetry install
    ```

2. Execute o scrapper utilizando o Makefile:
    ```sh
    make run
    ```

## Versão

version = "1.0.0"