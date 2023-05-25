from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import date

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    books = db.relationship('Book', backref='author', cascade='all, delete')


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))


class Animal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    type = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'animal',
        'polymorphic_on': type
    }


class Dog(Animal):
    __mapper_args__ = {
        'polymorphic_identity': 'dog'
    }
    breed = db.Column(db.String(50))


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    date = db.Column(db.Date, default=date.today)


# Configurar a URI do banco de dados MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/db_name'

# Criar todas as tabelas no banco de dados
db.create_all()

# Incluir um autor
author1 = Author(name='Author 1')
db.session.add(author1)
db.session.commit()

# Consultar todos os autores
authors = Author.query.all()
for author in authors:
    print(author.name)

# Consultar autores por filtro
authors_filtered = Author.query.filter_by(name='Author 1').all()
for author in authors_filtered:
    print(author.name)

# Alterar um autor
author1.name = 'New Author Name'
db.session.commit()

# Excluir um autor
db.session.delete(author1)
db.session.commit()

