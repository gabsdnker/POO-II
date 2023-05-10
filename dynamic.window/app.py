from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    idade = db.Column(db.Integer)

@app.route('/')
def index():
    dados = db.session.query(User).all() 
    return render_template('index.html', listagem=dados)

# CREATE - Criação de um novo usuário
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    name = request.form['nome']
    idade = request.form['idade']
    user = User(name=name, idade=idade)
    db.session.add(user)
    db.session.commit()
    return redirect("/")

# READ - Obtenção dos dados de todos os usuários
@app.route('/ler')
def ler():
    dados = db.session.query(User).all()
    return render_template('index.html', listagem=dados)

# UPDATE - Atualização de dados de um usuário
@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    user = db.session.query(User).get(id)
    user.name = request.form['nome']
    user.idade = request.form['idade']
    db.session.commit()
    return redirect("/")

# DELETE - Exclusão de um usuário
@app.route('/excluir/<int:id>')
def excluir(id):
    user = db.session.query(User).get(id)
    db.session.delete(user)
    db.session.commit()
    return redirect("/")

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
