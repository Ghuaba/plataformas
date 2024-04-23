import uuid
from app import db

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    estadoCivil = db.Column(db.String(50))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    censo_persona = db.relationship('Censo_persona', backref='persona', lazy=True)

    def __init__(self, name, lastName, edad, estadoCivil):
        self.name = name
        self.lastName = lastName
        self.edad = edad
        self.estadoCivil = estadoCivil

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_lastName(self):
        return self.lastName

    def set_lastName(self, lastName):
        self.lastName = lastName

    def get_edad(self):
        return self.edad

    def set_edad(self, edad):
        self.edad = edad

    def get_estadoCivil(self):
        return self.estadoCivil

    def set_estadoCivil(self, estadoCivil):
        self.estadoCivil = estadoCivil

    def get_external_id(self):
        return self.external_id

    def set_external_id(self, external_id):
        self.external_id = external_id
