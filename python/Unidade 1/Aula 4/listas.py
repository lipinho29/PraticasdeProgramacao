numeros = [10, 20, 30, 17, 58, 3, 7]
print(numeros[3])

print("-" * 60)

carros = ["Fusca", "Civic", "Onix", "Gol", "Palio"]
print('Temos o total de:', len(carros), 'carros')
print('1 ->', carros)

print("-" * 60)

carros.append("Corsa")
print('Temos o total de:', len(carros),'carros')
print('2 ->', carros)

print("-" * 60)

carros.remove("Onix")
print('Temos o total de:', len(carros), 'carros')
print('3 ->', carros)

print("-" * 60)

print('Você escolheu o seguinte carro:', carros[1])

print("-" * 60)

print('Você vendeu o carro:', carros[1])
del carros[1]
print('Temos o total de:', len(carros), 'carros')
print('4 ->', carros)

print("-" * 60)

carros = sorted(carros)
print('Carros em ordem alfabética:')
print('5 ->', carros)

print("-" * 60)

print(carros[0])
print(carros[1])
print(carros[2])
print(carros[3])

print("-" * 60)

for carro in carros:
    print(carro)
