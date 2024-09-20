from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import os
import sqlalchemy


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ba79b37d00047525a5e833980f864e91'
if os.getenv('DATABASE_URL'):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///projeto.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
#Redireciona as telas necessárias de login pra tela de login
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'
#Fica em baixo pois o init precisa chamar as rotas


from projcontrole import models
engine = sqlalchemy.create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
inspector = sqlalchemy.inspect(engine)
if not inspector.has_table('usuario'):
    with app.app_context():
        database.drop_all()
        database.create_all()
        print('Base de Dados criada')
else:
    print('Base de dados Existente')

from projcontrole import routes