import os.path

# Definindo o diretório base do projeto
B_DIR = os.path.abspath(os.path.dirname(__name__))

# Criando comunicação com a base de dados
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(B_DIR, 'fbStorage.db')
SQLALCHEMY_TRACK_MODIFICATIONS = True
