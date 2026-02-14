"""
app.route define a URL e qual a função a ser executada para cada URL.

Quando apenas '/' é especificado na URL, presume-se que seja a página inicial. 
Esta aplicação web fornecerá o texto '<h1>WELCOME to My Home Page</h1>'.
no estilo cabeçalho 1.  

Quando a URL contém um nome na URL, o nome da URL é analisado para ser usado 
na função que serve a página web. Esta é conhecida como uma "página web dinâmica". 

Quando o admin é específico na URL, o admin() será executado para 
redirecionar a página para mostrar a página inicial. 

Consulte as imagens abaixo para obter uma visão de como é cada página.
""" 


# Importar pacotes
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
  return "<h1>WELCOME to My Home Page</h1>"

@app.route("/<name>")
def user(name):
  return f"<h3>Hello, nice to meet you {name}!</h3>"

@app.route("/admin")
def admin():
  return redirect(url_for("home"))

if __name__ == "__main__":
  app.run()