from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/autogestion')
def autogestion():
    return render_template('autogestion.html')

@app.route('/colaboracion')
def colaboracion():
    return render_template('colaboracion.html')