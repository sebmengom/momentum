from app import app, db
from flask import render_template, request, redirect, url_for, flash
from app.models import Comment, Nombre


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/autogestion')
def autogestion():
    nombres = Nombre.query.all()
    return render_template('autogestion.html', nombres=nombres)

@app.route('/colaboracion')
def colaboracion():
    return render_template('colaboracion.html')

@app.route('/fotos')
def fotos():

    return render_template('fotos.html')

@app.route('/enviar_comentarios', methods=['POST'])
def enviar_comentarios():
    nombre = request.form.get('Nombre')
    comment = request.form.get('Comentario')

    if not nombre or not comment:
        flash('Por favor, rellena todos los campos')
        return redirect(url_for('autogestion'))
    else:
        n = Nombre(nombre=nombre)
        c = Comment(content=comment, nombre=n)
        db.session.add(n)
        n.comments.append(c)
        db.session.commit()
        return redirect(url_for('autogestion'))