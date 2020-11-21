from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail, Message

app = Flask(__name__)

app.config.from_pyfile('../config/config.cfg')
#SE SUPONE QUE CON LA LINEA DE ARRIBA CARGA EL CFG DONDE TENGO LO DEL MAIL CONFIGURADO

db = SQLAlchemy(app)
migrate = Migrate(app, db)

#EN LAS 2 LINEAS DE ABAJO SE SUPONE QUE HAGO UPDATE DE LOS SETTINGS DEL MAIL Y CREO EL OBJETO MAIL
#EL PARAM "MAIL_SETTING" DE ABAJO NO LO RECONOCE...
#PERO NO ENTIENDO POR QUE... PORQUE CARGO EL CFG ANTES
app.config.update(mail_settings)
mail = Mail(app)

from src.routes import routes
from src.models import user