import uuid
from datetime import datetime
from app import db

class MyTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    somecolumn = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, somecolumn):
        self.somecolumn = somecolumn

    def get_somecolumn(self):
        return self.somecolumn

    def set_somecolumn(self, somecolumn):
        self.somecolumn = somecolumn

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at
