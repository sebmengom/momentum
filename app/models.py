from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as orm
from app import db

class Nombre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(64), index=True, nullable=False)
    comments = db.relationship('Comment', back_populates='nombre', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<nombre {self.nombre}>'

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable = False)
    nombre_id = db.Column(db.Integer, db.ForeignKey('nombre.id'), nullable=False)
    nombre = db.relationship('Nombre', back_populates='comments')

    def __repr__(self):
        return f'<comment {self.content}>'