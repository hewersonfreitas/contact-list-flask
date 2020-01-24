# Lista Telefônica com Flask

Pequena aplicação exemplificando uma lista telefônica.

## Como executar o projeto

Iniciando ambiente virtual em Python

```sh
$ python -m venv contatct-list-flask

$ . ./contact-list-flask/bin/activate
```

Instalado as dependencias do projeto

```sh
$ pip install -r requirements.txt
```

Vamos executar os comandos abaixo partindo que esteja no diretório raiz onde fez o clone do projeto.

Definindo variaveis de ambiente:

```sh
$ export FLASK_APP=app
$ export FLASK_ENV=Development
$ export FLASK_DEBUG=True
```

Executando migrate do banco SQLite:

```sh
$ flask db init
$ flask db migrate
$ flask db upgrade
```

Executando o projeto: 
```sh
$ flask run
```

Acesse o projeto através do endereço:
```sh
http://localhost:5000
```