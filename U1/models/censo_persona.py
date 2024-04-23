import uuid
#from sqlalchemy.dialects.mysql import VARCHAR
from app import db

class Censo_persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date)
    longitud = db.Column(db.String(100))
    latitud = db.Column(db.String(100))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))


    #Llaves foraneas
    persona_id = db.Column(db.Integer, db.ForeignKey('persona.id'), nullable = False)
    censador_id = db.Column(db.Integer, db.ForeignKey('censador.id'), nullable = False)
    censo_id = db.Column(db.Integer, db.ForeignKey('censo.id'), nullable = False)