from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from app.models import Usuario
import sqlalchemy as sa
from sqlalchemy import select
from app import db

class LoginForm(FlaskForm):
    name = StringField('Ingrese "Momentum" para continuar', validators=[DataRequired()])
    password = PasswordField('El password sera dado en la presentacion.', validators=[DataRequired()])
    submit = SubmitField('Ingresar')
class RegisterForm(FlaskForm):
    name = StringField('Nombre', validators=[DataRequired()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Registrar')

    def validate_name(self, name):
        user = db.session.scalar(sa.select(Usuario).where(Usuario.usuario == name.data))
        if user is not None:
            raise ValidationError('El nombre de usuario ya esta en uso.')

