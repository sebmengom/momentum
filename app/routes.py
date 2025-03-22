from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    with open('app/static/data/intro.txt','r')as f:
        intro = f.read()
    return render_template('index.html', intro = intro)

@app.route('/autogestion')
def autogestion():
    with open('app/static/data/autogestion.txt','r') as f:
        autogestion = f.read()
    return render_template('autogestion.html', autogestion = autogestion)

@app.route('/colaboracion')
def colaboracion():
    with open('app/static/data/colaboracion.txt', 'r')as f:
        colaboracion = f.read()
    return render_template('colaboracion.html', colaboracion = colaboracion)