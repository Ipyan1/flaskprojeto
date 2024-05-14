from app import app
from flask import render_template
from flask import request

@app.route('/')# Configurando uma rota web
@app.route('/index')
def index():
    return render_template('index.html', titulo="Página Inicial", nome="Pâmela")

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo="Contato", nome="Pâmela")

@app.route('/buque')
def buque():
    return render_template('buque.html', titulo="Buquê de Flores", nome="Pâmela")

@app.route('/maisqueespeciais')
def maisqueespeciais():
    return render_template('maisqueespeciais', titulo="Mais que Especiais", nome="Pâmela")

@app.route('/cestas')
def cestas():
    return render_template('cestas.html', titulo="Cestas", nome="Pâmela")

@app.route('/encantadas')
def encantadas():
    return render_template('encantadas.html', titulo="Encantadas", nome="Pâmela")




