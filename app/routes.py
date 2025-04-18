from app import app, db, login
from app.forms import LoginForm, RegisterForm
from flask import render_template, request, redirect, url_for, flash
from app.models import Comment, Nombre, Usuario
from flask_login import current_user, login_user, logout_user, login_required
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from sqlalchemy import text

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/autogestion')
def autogestion():
    page = request.args.get('page', 1, type=int)
    per_page = app.config['COMMENTS_PER_PAGE']
    nombres = Nombre.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    return render_template('autogestion.html', pagination = nombres, nombres = nombres.items, endpoint = 'autogestion')

@app.route('/colaboracion')
def colaboracion():
    page = request.args.get('page', 1, type=int)
    per_page = app.config['COMMENTS_PER_PAGE']
    nombres = Nombre.query.paginate(
        page=page,
        per_page=per_page,
        error_out=False
    )
    return render_template('colaboracion.html', nombres = nombres.items, pagination = nombres, endpoint = 'colaboracion')

@app.route('/fotos')
@login_required
def fotos():
    return render_template('fotos.html')

@app.route('/enviar_comentarios', methods=['POST'])
def enviar_comentarios():
    fuente = request.form.get('fuente')
    nombre = request.form.get('Nombre')
    comment = request.form.get('Comentario')

    if not nombre or not comment:
        flash('Por favor, rellena todos los campos')
        return redirect(fuente)
    else:
        n = Nombre(nombre=nombre)
        c = Comment(content=comment, nombre=n)
        db.session.add(n)
        n.comments.append(c)
        db.session.commit()
        return redirect(fuente)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('fotos'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(Usuario).where(Usuario.usuario == form.usuario.data))
        if user is None or not user.check_password(form.password.data):
            flash('Usuario o contraseña incorrectos')
            return redirect(url_for('login'))
        login_user(user)
        return redirect(url_for('fotos'))
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('fotos'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = Usuario(usuario=form.usuario.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registro Exitoso')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/health')
def health_check():
    try:
        # Envuelve la consulta en text()
        db.session.execute(text('SELECT 1'))
        return '✅ Conectado a RDS correctamente'
    except Exception as e:
        return f'❌ Error de conexión: {e}'
