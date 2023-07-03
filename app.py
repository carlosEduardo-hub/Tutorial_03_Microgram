from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


#Criando o app
app = Flask(__name__)
#Configurando o SQLite database relativo a pasta da instância do aplicativo
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Tutorial03.sqlite3" 
#criando a extensão
db = SQLAlchemy()  
#Inicializando o app com a extensãosS
db.init_app(app)

#Outra forma de criar a extensão e inicializar o app
#db = SQLAlchemy(app)

class cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    ch = db.Column(db.Integer)

    def __init__(self, nome, descricao, ch):
        self.nome = nome
        self.descricao = descricao
        self.ch = ch

@app.route('/cursos')
def lista_cursos():
    page = request.args.get('page', 1, type=int)
    per_page = 4
    todos_cursos = cursos.query.paginate(page=page, per_page=per_page)
    return render_template("cursos.html", cursos=todos_cursos)


with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)