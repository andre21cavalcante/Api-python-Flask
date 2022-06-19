from flask import Flask, Response, request
from flask_sqlalchemy import SQLAlchemy
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/pessoas'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(100))
    telefone = db.Column(db.String(100))

    def to_json(self):
        return {"id": self.id, "nome": self.nome, "email": self.email, "telefone": self.telefone}

# selecionar tudo

@app.route("/users", methods=["GET"])
def seleciona_users():
    usuarios_objetos = Usuario.query.all()
    usuarios_json = [users.to_json() for users in usuarios_objetos]

    return gera_response(200,"users", usuarios_json, "todos os usuarios ok")

# selecionar um usuario chamando por id
@app.route("/user/<id>")
def seleciona_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    usuario_json = usuario_objeto.to_json()

    return gera_response(200, "user", usuario_json, "usuario encontrado")

# cadastrar

# atualizar 
# deletar

def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem 
        
    return Response(json.dumps(body), status=status, mimetype="application/json")

app.run()