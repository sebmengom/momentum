from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Usuario
import sqlalchemy as sa
from sqlalchemy import select
from app import db

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    usuario = StringField('Usuario', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar sesión')

class RegisterForm(FlaskForm):
    usuario = StringField('Nombre', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    def validate_usuario(self, usuario):  
        user = db.session.scalar(sa.select(Usuario).where(Usuario.usuario == usuario.data))
        if user is not None:
            raise ValidationError('El nombre de usuario ya esta en uso.')
