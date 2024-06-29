# Projeto CRUD em Python com PostgreSQL

Este projeto em Python demonstra operações básicas de CRUD (Create, Read, Update, Delete) em um banco de dados PostgreSQL utilizando a biblioteca psycopg2.

## Funcionalidades

- **Inserção de Dados:** Permite adicionar novos registros de produtos ao banco de dados.
- **Leitura de Dados:** Recupera todos os registros de vendas do banco de dados.
- **Atualização de Dados:** Permite atualizar o valor de um produto existente no banco de dados.
- **Exclusão de Dados:** Remove um produto do banco de dados com base no nome do produto.

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter os seguintes requisitos instalados:

- Python 
- PostgreSQL
- psycopg2 (pode ser instalado via pip: `pip install psycopg2`)

## Estrutura do Projeto
A estrutura de diretórios do projeto é a seguinte:

├── README.md

├── crud/

    └──  insert.py
    └──  read.py                 
    └──  update.py
    └──  delete.py

├── .gitignore

    └── config.py


### Instruções para Personalização:

- Substitua as seções `nome_do_banco_de_dados`, `localhost`, `usuario_do_banco` e `senha_do_banco` no arquivo `config.py` com suas próprias configurações de banco de dados.
- Personalize os comandos de execução (inserção, leitura, atualização, exclusão) de acordo com a estrutura e o nome dos seus scripts Python.
- Verifique se a estrutura de diretórios (`crud/`, `config.py`, `.gitignore`) reflete exatamente a estrutura do seu projeto.
