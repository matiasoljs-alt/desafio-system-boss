 CRUD de Usuários e Notas com FastAPI

Descrição

API REST desenvolvida com FastAPI, SQLModel e SQLite para gerenciamento de usuários e notas.

Cada usuário pode possuir várias notas associadas.

Tecnologias Utilizadas

- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn

Estrutura do Projeto

system boss/
│
├── main.py
├── database.py
├── dependencies.py
├── models.py
├── schemas.py
│
└── routers/
    ├── user.py
    └── note.py

Instalação

Clone o repositório:

git clone <url-do-repositorio>
cd system-boss

Instale as dependências:

pip install -r requirements.txt

Executando a API

uvicorn main:app --reload

A API ficará disponível em:

http://127.0.0.1:8000

Documentação automática:

http://127.0.0.1:8000/docs

Rotas

Criar Usuário

POST /create_user

Body:

{
  "nome": "Matias",
  "email": "matias@email.com"
}

Listar Usuários

GET /_users

Buscar Usuário por ID

GET /find_user/{user_id}

Exemplo:

GET /find_user/1

Deletar Usuário

DELETE /user_delete/{user_id}

Exemplo:

DELETE /user_delete/1

Criar Nota para um Usuário

POST /user/{user_id}/notes

Body:

{
  "title": "Minha Nota",
  "conteudo": "Conteúdo da nota"
}

Exemplo:

POST /user/1/notes

Funcionalidades

- Criar usuários
- Listar usuários
- Buscar usuário por ID
- Deletar usuários
- Criar notas associadas a um usuário
