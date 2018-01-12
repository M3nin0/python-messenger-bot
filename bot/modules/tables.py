from bot import db

class User(db.Model):
    '''
        Classe da entidade dos usuários no banco de dados
        :extends db.Model (Modelo)
    '''

    __tablename__ = 'users'

    # Colunas
    _id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    gender = db.Column(db.String(6))


    # Definindo propriedades requiridas pelo SqlAlchemy    
    @property
    def is_authenticated(self):
        return True


    @property
    def is_active(self):
        return True


    @property
    def get_id(self):
        return str(self._id)


    # Sobrescreve método de representação dos objetos
    def __repr__(self):
        return self.first_name
    

    def __init__(self, _id, first_name, last_name, gender):
        self._id = _id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
