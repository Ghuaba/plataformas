import uuid
#from sqlalchemy.dialects.mysql import VARCHAR
from app import db
'''
class Censador(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    dni = db.Column(db.Integer)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))

    censo = db.relationship('Censo', backref = 'censador', lazy=True)
'''

#sirve pero hay una una forma mas elegante
class Censador(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    dni = db.Column(db.Integer)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))

    censo_persona = db.relationship('Censo_persona', backref='censador', lazy=True)



    def __init__(self, name, lastName, dni):
        self.name = name
        self.lastName = lastName
        self.dni = dni

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_lastName(self):
        return self.lastName

    def set_lastName(self, lastName):
        self.lastName = lastName

    def get_dni(self):
        return self.dni

    def set_dni(self, dni):
        self.dni = dni

    def get_external_id(self):
        return self.external_id

    def set_external_id(self, external_id):
        self.external_id = external_id




'''
class Censador(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    _name = db.Column(db.String(100))
    _lastName = db.Column(db.String(100))
    _dni = db.Column(db.Integer)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))

    censo_persona = db.relationship('Censo_persona', backref='censador', lazy=True)

    def __init__(self, name, lastName, dni):
        self._name = name
        self._lastName = lastName
        self._dni = dni

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def lastName(self):
        return self._lastName

    @lastName.setter
    def lastName(self, lastName):
        self._lastName = lastName

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    @property
    def external_id(self):
        return self.external_id

    @external_id.setter
    def external_id(self, external_id):
        self.external_id = external_id
'''