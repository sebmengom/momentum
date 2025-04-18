from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

@login.user_loader
def load_user(id):
    return db.session.get(Usuario, int(id))

class Nombre(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    nombre: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, nullable=False)
    comments: so.Mapped[list['Comment']] = so.relationship(back_populates='nombre')

    def __repr__(self):
        return f'<nombre {self.nombre}>'

class Comment(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    content: so.Mapped[str] = so.mapped_column(sa.String(200), nullable=False)
    
    nombre_id: so.Mapped[int] = so.mapped_column(sa.ForeignKey('nombre.id'), nullable=False)
    nombre: so.Mapped['Nombre'] = so.relationship(back_populates='comments')

    def __repr__(self):
        return f'<comment {self.content}>'

class Usuario(UserMixin, db.Model):
    id:so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    usuario : so.Mapped[str] = so.mapped_column(sa.String(64), index=True, nullable=False, unique=True)
    password_hash :so.Mapped[str] = so.mapped_column(sa.String(200), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
        print(f'Password hash: {self.password_hash}')
        print(f'Password: {password}')
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<Usuario {self.usuario}>'