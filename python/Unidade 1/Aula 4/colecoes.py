# conjuntos
conjunto = set([4, 7, 2, 3, 0, 8])
print("Conjunto:", conjunto)

#tupla
tupla = (4, 7, 2, 3, 0, 8)
print("Tupla:", tupla)

pessoas = ['Filipe', 'João', 'Maria', 'Ana']
print("Lista de pessoas:", pessoas)

pessoa = {'nome': 'Filipe', 'idade': 30, 'cidade': 'Lisboa'}
print(pessoa['nome'])

pessoas2 = [
    {'nome': 'Filipe', 'idade': 30, 'cidade': 'Lisboa'},
    {'nome': 'João', 'idade': 25, 'cidade': 'Porto'},
    {'nome': 'Maria', 'idade': 28, 'cidade': 'Coimbra'},
    {'nome': 'Ana', 'idade': 22, 'cidade': 'Braga'}
    ]

print("Lista de dicionários:", pessoas2)
print(pessoas2[0]['idade'])