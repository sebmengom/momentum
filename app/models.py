from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app import db

class nombre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), index=True, unique=True, nullable=False)
    apellido = db.Column(db.String(64), index=True, unique=True, nullable=False)
    
    def __repr__(self):
        return f'<nombre {self.nombre} {self.apellido}>'

class comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    nombre = db.relationship('nombre', backref='comments')

    def __repr__(self):
        return f'<comment {self.content}>'