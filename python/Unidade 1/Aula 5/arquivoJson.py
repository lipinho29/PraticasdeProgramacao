import json

pessoas = [
    {'nome': 'Joao', 'idade': 30, 'cidade': 'Sao Paulo'},
    {'nome': 'Maria', 'idade': 25, 'cidade': 'Rio de Janeiro'},
    {'nome': 'Pedro', 'idade': 28, 'cidade': 'Belo Horizonte'},
    {'nome': 'Ana', 'idade': 22, 'cidade': 'Curitiba'},
    {'nome': 'Lucas', 'idade': 35, 'cidade': 'Porto Alegre'},
]

with open('pessoas.json', 'w') as arquivo:
    json.dump(pessoas, arquivo, indent=4, ensure_ascii=False)