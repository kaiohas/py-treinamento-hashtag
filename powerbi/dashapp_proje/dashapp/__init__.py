
from dash import Dash
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy


app = Dash(__name__)
server = app.server
app.config.suppress_callback_exceptions = True

server.config.update(
    SQLALCHEMY_DATABASE_URI="sqlite:///bancodedados.db",
    SECRET_KEY = "machadoalvessiqueirakaio",
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

database = SQLAlchemy(server)
Bcrypt = Bcrypt(server)
login_manager = LoginManager(server)
login_manager.login_view = "/login"

from dashapp import views

