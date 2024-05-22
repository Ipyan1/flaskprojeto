import requests

from app import app
from flask import render_template
from flask import request
import json
import requests
link ="https://flaskti18n-e3938-default-rtdb.firebaseio.com/"
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

@app.route('/cadastro')
def cadastrar():
    return render_template('cadastro.html', titulo='cadastro')

@app.route('/cadastrarUsuário', methods=['POST'])
def cadastrarUsusario():
    try:
        cpf       =request.form.get("cpf")
        nome      =request.form.get("nome")
        telefone  =request.form.get("telefone")
        endereço  =request.form.get("endereço")
        dados     ={"cpf":cpf,"nome":nome, "telefone":telefone, "endereço":endereço}
        requisicao= request.post(f'{link}/cadastrar/.json', data=json.dumps(dados))
        return 'Cadastrado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n\n = {e}'

@app.route('/listar')
def listarTudo():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json') #Solicitar Dados do Banco
        dicionario = requests.json()

    except Exception as e:
        return f'Ocorreu um erro\n\n = {e}'

@app.route('/listarIndividual')
def listarIndividual():
    try:
        requisicao = requests.get(f'{link}/cadastrar/.json')
        dicionario = requests.json()
        idCadastro = ""
        for codigo in dicionario:
        usuario= dicionario[codigo]['cpf']
            if(cpf="1231"):
            idCadastro = codigo
    except Exception as e:
        return f'Ocorreu um erro\n\n = {e}'

     #id para copiar para atualizar
@app.route('/atualizar')
def atualizar():
    try:
        dados = {"nome": "Gabriel"}#Parâmetro para atualização
        requesicao = requests.patch(f'{link}/cadastrar/-#colocar oid/json', data=json.dumps(dados))
        return 'Cadastro realizado com sucesso!'
    except Exception as e:
        return f'Ocorreu um erro\n\n = {e}'

@app.route('/excluir')
def excluir():
    try:
        requisicao = requests.delete(f'{link}/cadastrar/ # colocar o id/json')
        return ' Excluido com Sucesso!'
    except Exception as e:
        return f'Houve um erro\n\n = {e}'




