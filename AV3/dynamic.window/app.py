from flask import Flask, render_template, request, redirect, url_for, jsonify, flash
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.secret_key = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
db = SQLAlchemy(app)

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    columns = db.relationship('Column', backref='table', lazy='dynamic', cascade='all, delete-orphan')
    rows = db.relationship('Row', backref='table', lazy='dynamic', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Table {self.name}>"

class Column(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))

    def __repr__(self):
        return f"<Column {self.name}>"

class Row(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'))
    cells = db.relationship('Cell', backref='row', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Row {self.id}>"

class Cell(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    row_id = db.Column(db.Integer, db.ForeignKey('row.id'))
    column_id = db.Column(db.Integer, db.ForeignKey('column.id'))
    value = db.Column(db.String(255))

    column = db.relationship('Column', backref='cells')

    def __repr__(self):
        return f"<Cell {self.value}>"

@app.route('/')
def index():
    tables = Table.query.all()
    return render_template('index.html', tables=tables)

@app.route('/create_table', methods=['GET', 'POST'])
def create_table():
    if request.method == 'POST':
        name = request.form['name']
        table = Table(name=name)
        db.session.add(table)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create_table.html')

@app.route('/edit_table/<int:table_id>', methods=['GET', 'POST'])
def edit_table(table_id):
    table = Table.query.get_or_404(table_id)
    
    if request.method == 'POST':
        table.name = request.form['name']
        db.session.commit()
    
    return render_template('edit_table.html', table_id=table_id, table=table)

@app.route('/delete_table/<int:table_id>', methods=['POST'])
def delete_table(table_id):
    table = Table.query.get_or_404(table_id)
    db.session.delete(table)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_column/<int:table_id>', methods=['GET', 'POST'])
def add_column(table_id):
    table = Table.query.get_or_404(table_id)
    if request.method == 'POST':
        name = request.form['name']
        column = Column(name=name, table=table)
        db.session.add(column)
        db.session.commit()
        return redirect(url_for('edit_table', table_id=table_id))
    return render_template('add_column.html', table=table)

@app.route('/delete_column/<int:column_id>', methods=['POST'])
def delete_column(column_id):
    column = Column.query.get_or_404(column_id)
    table_id = column.table.id
    db.session.delete(column)
    db.session.commit()
    return redirect(url_for('edit_table', table_id=table_id))

@app.route('/add_row/<int:table_id>', methods=['POST'])
def add_row(table_id):
    table = Table.query.get(table_id)
    if table is None:
        flash('Tabela não encontrada.', 'error')
        return redirect(url_for('edit_table', table_id=table_id))
    row = Row(table_id=table_id)
    db.session.add(row)
    db.session.commit()
    flash('Linha adicionada com sucesso.', 'success')
    return redirect(url_for('edit_table', table_id=table_id))

@app.route('/delete_row/<int:row_id>', methods=['POST'])
def delete_row(row_id):
    row = Row.query.get(row_id)
    if row is None:
        flash('Linha não encontrada.', 'error')
        return redirect(url_for('edit_table', table_id=row.table_id))
    db.session.delete(row)
    db.session.commit()
    flash('Linha excluída com sucesso.', 'success')
    return redirect(url_for('edit_table', table_id=row.table_id))

@app.route('/add_cell/<int:table_id>/<int:column_id>/<int:row_id>', methods=['POST'])
def add_cell(table_id, column_id, row_id):   
    row = Row.query.get_or_404(row_id)
    value = request.form['value']
    cell = Cell.query.filter_by(row=row, column_id=column_id).first()
    
    if cell:
        cell.value = value
    else:
        cell = Cell(row=row, column_id=column_id, value=value)
        db.session.add(cell)
    
    db.session.commit()
    return redirect(url_for('edit_table', table_id=table_id))

@app.route('/delete_cell/<int:table_id>/<int:column_id>/<int:row_id>', methods=['POST'])
def delete_cell(table_id, column_id, row_id):
    row = Row.query.get_or_404(row_id)
    column = Column.query.get_or_404(column_id)
    cell = Cell.query.filter_by(row=row, column=column).first()
    
    if cell:
        db.session.delete(cell)
        db.session.commit()
        flash('Célula excluída com sucesso.', 'success')
    else:
        flash('Célula não encontrada.', 'error')
    
    return redirect(url_for('edit_table', table_id=table_id))

@app.route('/show_cell/<int:table_id>/<int:column_id>/<int:row_id>')
def show_cell(table_id, column_id, row_id):
    row = Row.query.get_or_404(row_id)
    column = Column.query.get_or_404(column_id)
    cell = Cell.query.filter_by(row=row, column=column).first()

    if cell is None:
        flash('Célula não encontrada.', 'error')
        return redirect(url_for('edit_table', table_id=table_id))
    return render_template('edit_table.html', table_id=table_id)

@app.route('/show_tables')
def show_tables():
    tables = Table.query.all()
    return render_template('show_tables.html', tables=tables)

@app.route('/get_table_data/<int:table_id>', methods=['GET'])
def get_table_data(table_id):
    table = Table.query.get_or_404(table_id)
    columns = table.columns
    table_data = []

    for row in table.rows:
        cell_data = {}
        for column in columns:
            cell = Cell.query.filter_by(row=row, column=column).first()
            if cell:
                cell_data[column.name] = cell.value
            else:
                cell_data[column.name] = ""
        table_data.append(cell_data)

    data = {
        'table_name': table.name,
        'columns': [column.name for column in columns],
        'table_data': table_data
    }
    return jsonify(data)

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
