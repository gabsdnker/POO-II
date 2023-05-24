from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from builtins import getattr

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)

class GenericTable(db.Model):
    __tablename__ = 'generic_table'
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, **kwargs):
        for column, value in kwargs.items():
            setattr(self, column, value)

@app.route('/')
def index():
    dados = db.session.query(GenericTable).all() 
    return render_template('index.html', listagem=dados)

# CREATE - Criação de um novo registro
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome_tabela = request.form['tabela']
    campos = request.form.getlist('campo')
    valores = request.form.getlist('ID')

    # Cria um novo registro na tabela especificada
    nova_tabela = type(nome_tabela, (GenericTable,), {})
    novo_registro = nova_tabela(**dict(zip(campos, valores)))
    db.session.add(novo_registro)
    db.session.commit()

    return redirect("/")

# READ - Obtenção dos dados de todos os registros
@app.route('/ler')
def ler():
    dados = db.session.query(GenericTable).all()
    return render_template('index.html', listagem=dados)

# UPDATE - Atualização de dados de um registro
@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(Id):
    registro = db.session.query(GenericTable).get(Id)

    # Atualiza os campos do registro
    for campo in request.form:
        setattr(registro, campo, request.form[campo])
    db.session.commit()
    return redirect("/")

# DELETE - Exclusão de um registro
@app.route('/excluir/<int:id>')
def excluir(Id):
    registro = db.session.query(GenericTable).get(Id)
    db.session.delete(registro)
    db.session.commit()
    return redirect("/")

@app.route('/tabelas')
def tabelas():
    tabelas = db.session.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
    tabelas = [tabela[0] for tabela in tabelas]
    return render_template('/', tabelas=tabelas)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
