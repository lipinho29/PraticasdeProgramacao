import numpy as np

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Calculando a média "na mão"
soma = 0

for n in numeros:
    soma += n

print('Soma total dos números é:', soma)

media = soma / len(numeros)
print('Média na mão:', media)

# Usando Numpy
array_numeros = np.array(numeros)

media = np.mean(array_numeros)
print('Média com Numpy:', media)
