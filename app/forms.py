from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    name = StringField('Ingrese "Momentum" para continuar', validators=[DataRequired()])
    password = PasswordField('El password sera dado en la presentacion.', validators=[DataRequired()])