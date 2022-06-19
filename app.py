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
@app.route("/user/<id>", methods=["GET"])
def seleciona_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    usuario_json = usuario_objeto.to_json()

    return gera_response(200, "user", usuario_json, "usuario encontrado")

# Criando endpoint de adicionar usuario
@app.route("/user", methods=["POST"])
def add_user():
    body = request.get_json()

    try:
        user = Usuario(nome=body["nome"], email= body["email"], telefone= body["telefone"])
        db.session.add(user)
        db.session.commit()
        return gera_response(201, "user", user.to_json(), "usuario adicionado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "user", {}, "erro ao adicionar")


# atualiza informaçoes do usuario
@app.route("/user/<id>", methods=["PUT"])
def atualiza_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()
    body = request.get_json()

    try:
        if('nome' in body):
            usuario_objeto.nome = body['nome']
        if('email' in body):
            usuario_objeto.email = body['email']
        if('telefone' in body):
            usuario_objeto.telefone = body['telefone']

        db.session.add(usuario_objeto)
        db.session.commit() 
        return gera_response(200, "user", usuario_objeto.to_json(), "atualiado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "user", {}, "erro ao atualizar")


# Deleta usuario
@app.route("/user/<id>", methods=["DELETE"])
def deleta_usuario(id):
    usuario_objeto = Usuario.query.filter_by(id=id).first()

    try:
        db.session.delete(usuario_objeto)
        db.session.commit()
        return gera_response(200, "user", usuario_objeto.to_json(), "User Deletado com sucesso")
    except Exception as e:
        print(e)
        return gera_response(400, "user", {}, "erro ao detelar")


def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem):
        body["mensagem"] = mensagem 
        
    return Response(json.dumps(body), status=status, mimetype="application/json")

app.run()