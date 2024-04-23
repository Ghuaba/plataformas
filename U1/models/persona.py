import uuid
#from sqlalchemy.dialects.mysql import VARCHAR
from app import db

class Persona(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastName = db.Column(db.String(100))
    edad = db.Column(db.Integer)
    estadoCivil = db.Column(db.String(50))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    censo_persona = db.relationship('Censo_persona', backref = 'persona', lazy=True)