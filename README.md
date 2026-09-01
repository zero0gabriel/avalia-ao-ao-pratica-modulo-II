# avalia-ao-ao-pratica-modulo-II
# 🎮 Sistema de Cadastro de Jogos

## 📖 Sobre o Projeto

Este projeto foi desenvolvido como parte da avaliação prática do curso de **Python**, utilizando o framework **Flask** e o banco de dados **SQLite**.

A aplicação permite realizar o gerenciamento de um catálogo de jogos por meio das operações básicas de um sistema CRUD (Create, Read, Update e Delete).

## 🚀 Funcionalidades

* ✅ Cadastrar novos jogos
* ✅ Listar todos os jogos cadastrados
* ✅ Editar informações de um jogo
* ✅ Excluir jogos do catálogo
* ✅ Armazenar:

  * Nome do jogo
  * Gênero
  * Nota
  * URL da imagem

## 🛠️ Tecnologias Utilizadas

* Python 3
* Flask
* SQLite
* HTML
* CSS

## 📂 Estrutura do Projeto

```text
projeto/
│
├── app.py
├── jogos.db
├── templates/
│   ├── index.html
│   └── editar.html
├── static/
│   └── style.css
└── README.md
```

## ⚙️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
```

### 2. Acesse a pasta do projeto

```bash
cd seu-repositorio
```

### 3. Instale as dependências

```bash
pip install flask
```

### 4. Execute a aplicação

```bash
python app.py
```

### 5. Abra no navegador

```
http://127.0.0.1:5000
```

## 🗄️ Banco de Dados

O projeto utiliza o **SQLite**, criando automaticamente o arquivo `jogos.db` caso ele ainda não exista.

A tabela criada possui os seguintes campos:

| Campo      | Tipo    |
| ---------- | ------- |
| id         | INTEGER |
| nome       | TEXT    |
| genero     | TEXT    |
| nota       | REAL    |
| imagem_url | TEXT    |

## 📚 Conceitos Aplicados

Durante o desenvolvimento foram utilizados os seguintes conceitos:

* Flask
* Rotas
* Templates HTML (Jinja2)
* Formulários
* SQLite
* CRUD
* Funções em Python
* Conexão com banco de dados
* Redirecionamento entre páginas

## 🎯 Objetivo

O objetivo deste projeto foi colocar em prática os conhecimentos adquiridos durante o curso de Python, desenvolvendo uma aplicação web capaz de realizar operações completas de cadastro, edição, consulta e exclusão de registros utilizando Flask e SQLite.

## 👨‍💻 Autor

Projeto desenvolvido como atividade avaliativa do curso de Python.
