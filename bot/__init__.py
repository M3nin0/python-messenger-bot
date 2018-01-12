'''
    Pacote contendo as instâncias do projeto
'''

from flask import Flask
from flask_script import Manager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import MigrateCommand

app = Flask(__name__)
app.config.from_object('bot.config.config')

# Configurando banco de dados
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Configurando o meneger da aplicação
manager = Manager(app)
manager.add_command('db', MigrateCommand)