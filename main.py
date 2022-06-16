from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio')
def cardapio():
  arquivo = open("static/pizzas.json")
  pizzas = json.load(arquivo)
  return render_template('cardapio.html', promocao=False, pizzas=pizzas)

@app.route('/avaliacoes')
def avaliacoes():
  clientes = [
    {'nome': 'Maria', 'nota': 5},
    {'nome': 'José', 'nota': 3},
    {'nome': 'Pedro', 'nota': 4},
    {'nome': 'Bianca', 'nota': 3},
    {'nome': 'Lorena', 'nota': 2},  
  ]
  return render_template('avaliacoes.html', clientes=clientes)

@app.route('/faleconosco')
def faleconosco():
    return render_template('faleconosco.html')

@app.route('/login')
def login():
    return render_template('login.html')

app.run(host='0.0.0.0', port=81)