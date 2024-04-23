import uuid
#from sqlalchemy.dialects.mysql import VARCHAR
from app import db

class Censo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.Boolean, default = True)
    fechaInicio = db.Column(db.Date)
    fechaFin = db.Column(db.Date)
    motivo = db.Column(db.String(100))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
    