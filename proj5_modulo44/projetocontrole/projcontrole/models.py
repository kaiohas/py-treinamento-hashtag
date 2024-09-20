from datetime import datetime
from projcontrole import database, login_manager
from flask_login import UserMixin


#função criada para localizar o login.
@login_manager.user_loader
def load_usuario(id_usuario):
    #Aqui é usado o metodo .get na query, pois estamos buscando o id
    return Usuario.query.get(int(id_usuario))

# Usermixin é necessário para classificar essa tabela como controloadora dos logins.
class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    usuario =  database.Column(database.String, nullable=False)
    email =  database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)
    foto_perfil = database.Column(database.String, default='default.png')
    posts = database.relationship('Post', backref='autor', lazy=True)
    cursos = database.Column(database.String, nullable=False, default="Não informado")

    def contar_posts(self):
        return len(self.posts)





class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String, nullable=False)
    corpo =  database.Column(database.Text, nullable=False)
    data_criacao =  database.Column(database.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
