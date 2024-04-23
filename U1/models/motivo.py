import uuid
#from sqlalchemy.dialects.mysql import VARCHAR
from app import db
from enum import Enum
class Motivo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    motivo = db.Column(db.String(100))
    external_id = db.Column(db.VARCHAR(60), default=str(uuid.uuid4()))
