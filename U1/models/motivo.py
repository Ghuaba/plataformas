import uuid
from app import db

class Motivo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), unique=True, nullable=False)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))

    def __init__(self, nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_external_id(self):
        return self.external_id

    def set_external_id(self, external_id):
        self.external_id = external_id
