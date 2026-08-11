# Sistema de Biblioteca API

API REST desenvolvida em Python com FastAPI para gerenciamento de livros.

O projeto permite cadastrar, listar, buscar, atualizar e excluir livros, utilizando SQLite para persistência de dados e Pydantic para validação.

## Tecnologias

- Python
- FastAPI
- SQLite
- Pydantic
- Uvicorn
- Swagger / OpenAPI

## Funcionalidades

- Cadastro de livros
- Listagem de livros
- Busca por ID
- Atualização de livros
- Exclusão de livros
- Validação de dados
- Tratamento de erros HTTP
- Documentação automática com Swagger

## Estrutura do projeto

```text
sistema_biblioteca/
│
├── main.py
├── crud.py
├── database.py
├── models.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Como executar

Clone o repositório:

```bash
git clone git@github.com:DevPatrick-code/sistema-biblioteca-fastapi.git
```

Entre na pasta do projeto:

```bash
cd sistema-biblioteca-fastapi
```

Crie o ambiente virtual:

```bash
python -m venv .venv
```

Ative no Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie a API:

```bash
uvicorn main:app --reload
```

A API estará disponível em:

http://127.0.0.1:8000

Documentação

Com a aplicação rodando, acesse:

http://127.0.0.1:8000/docs

A documentação interativa é gerada automaticamente pelo FastAPI com Swagger UI.

## Endpoints

| Método | Endpoint | Descrição |
|---|---|---|
| GET | `/livros` | Lista todos os livros |
| GET | `/livros/{id}` | Busca um livro por ID |
| POST | `/livros` | Cadastra um novo livro |
| PUT | `/livros/{id}` | Atualiza um livro |
| DELETE | `/livros/{id}` | Exclui um livro |

## Exemplo de cadastro

```json
{
  "id": 1,
  "titulo": "O Senhor dos Anéis",
  "autor": "J.R.R. Tolkien",
  "disponivel": true,
  "ano": 1954
}
```

## Validações

A API possui validações como:

- ID deve ser maior que zero
- título não pode estar vazio
- autor não pode estar vazio
- espaços extras são removidos de título e autor
- ano deve ser maior que zero
- ano não pode ser maior que o ano atual
- disponibilidade deve ser um valor booleano

## Status HTTP utilizados

- `200 OK`
- `201 Created`
- `404 Not Found`
- `409 Conflict`
- `422 Unprocessable Entity`

## Objetivo

Este projeto foi desenvolvido com foco em aprendizado de desenvolvimento backend, APIs REST, persistência de dados, validação e boas práticas de organização de código.

## Autor

Desenvolvido por **Patrick Alves**.


