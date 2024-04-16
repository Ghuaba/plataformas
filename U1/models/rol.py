from app import db

class Rol(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(100))
    estado = db.Column(db.Boolean, default = True)
    external_id = db.Column(db.String(60))
    
    