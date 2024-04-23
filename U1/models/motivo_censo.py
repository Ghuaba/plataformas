import uuid
#from sqlalchemy.dialects.mysql import VARCHAR
from app import db

class Motivo_censo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descripcion = db.Column(db.String(100))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))

    censo_persona_id = db.Column(db.Integer, db.ForeignKey('censo_persona.id'), nullable = False)

    motivo_id = db.Column(db.Integer, db.ForeignKey('motivo.id'))
    motivo = db.relationship('Motivo', backref='motivo_senso')
   
''' motivo_id = db.Column(db.Integer, db.ForeignKey('catalogo.id'))
    motivo = db.relationship('Motivo', backref= 'motivo')'''
    