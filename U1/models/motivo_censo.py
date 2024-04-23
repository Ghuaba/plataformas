import uuid
from app import db
from models.motivo import Motivo

class Motivo_censo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100))
    motivo_id = db.Column(db.Integer, db.ForeignKey('motivo.id'), nullable=False)
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    censo_persona_id = db.Column(db.Integer, db.ForeignKey('censo_persona.id'), nullable=False)

    def __init__(self, descripcion, motivo_id, censo_persona_id):
        self.descripcion = descripcion
        self.motivo_id = motivo_id
        self.censo_persona_id = censo_persona_id

    def get_descripcion(self):
        return self.descripcion

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion

    def get_motivo_id(self):
        return self.motivo_id

    def set_motivo_id(self, motivo_id):
        self.motivo_id = motivo_id

    def get_external_id(self):
        return self.external_id

    def set_external_id(self, external_id):
        self.external_id = external_id

    def get_censo_persona_id(self):
        return self.censo_persona_id

    def set_censo_persona_id(self, censo_persona_id):
        self.censo_persona_id = censo_persona_id
