import uuid
from app import db

class Censo_persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    longitud = db.Column(db.String(100))
    latitud = db.Column(db.String(100))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))

    # Llaves foraneas
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable=False)
    censo_id = db.Column(db.Integer, db.ForeignKey('censo.id'), nullable=False)
    censador_id = db.Column(db.Integer, db.ForeignKey('censador.id'), nullable=False)

    def __init__(self, fecha, longitud, latitud, persona_id, censo_id, censador_id):
        self.fecha = fecha
        self.longitud = longitud
        self.latitud = latitud
        self.persona_id = persona_id
        self.censo_id = censo_id
        self.censador_id = censador_id

    def get_fecha(self):
        return self.fecha

    def set_fecha(self, fecha):
        self.fecha = fecha

    def get_longitud(self):
        return self.longitud

    def set_longitud(self, longitud):
        self.longitud = longitud

    def get_latitud(self):
        return self.latitud

    def set_latitud(self, latitud):
        self.latitud = latitud

    def get_external_id(self):
        return self.external_id

    def set_external_id(self, external_id):
        self.external_id = external_id

    def get_persona_id(self):
        return self.persona_id

    def set_persona_id(self, persona_id):
        self.persona_id = persona_id

    def get_censo_id(self):
        return self.censo_id

    def set_censo_id(self, censo_id):
        self.censo_id = censo_id

    def get_censador_id(self):
        return self.censador_id

    def set_censador_id(self, censador_id):
        self.censador_id = censador_id
