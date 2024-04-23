import uuid
from app import db

class Censo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.Boolean, default=True)
    fechaInicio = db.Column(db.Date)
    fechaFin = db.Column(db.Date)
    motivo = db.Column(db.String(100))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))

    censo_persona = db.relationship('Censo_persona', backref='censo', lazy=True)

    def __init__(self, estado, fechaInicio, fechaFin, motivo):
        self.estado = estado
        self.fechaInicio = fechaInicio
        self.fechaFin = fechaFin
        self.motivo = motivo

    def get_estado(self):
        return self.estado

    def set_estado(self, estado):
        self.estado = estado

    def get_fechaInicio(self):
        return self.fechaInicio

    def set_fechaInicio(self, fechaInicio):
        self.fechaInicio = fechaInicio

    def get_fechaFin(self):
        return self.fechaFin

    def set_fechaFin(self, fechaFin):
        self.fechaFin = fechaFin

    def get_motivo(self):
        return self.motivo

    def set_motivo(self, motivo):
        self.motivo = motivo

    def get_external_id(self):
        return self.external_id

    def set_external_id(self, external_id):
        self.external_id = external_id
