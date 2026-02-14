n1 = 7
n2 = 9
aprovado = True
media = 6
minimo = 7

print("Operadores Aritméticos")

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
exponenciacao = n1 ** n2
resto = n1 % n2

print('Soma: ', soma)
print('Subtração: ', subtracao)
print('Multiplicação: ', multiplicacao)
print('Divisão: ', divisao)
print('Divisão Inteira: ', divisao_inteira)
print('Exponenciação: ', exponenciacao)
print('Resto: ', resto)

print()
print("Operadores Relacionais")
print("Igualdade", n1 == n2)
print("Diferença", n1 != n2)
print("Maior que", n1 > n2)
print("Menor que", n1 < n2)
print("Maior ou igual a", n1 >= n2)
print("Menor ou igual a", n1 <= n2)

print()
print("Operadores Lógicos")
print(aprovado)
print (not aprovado)
print(n1 >= 7 and minimo == 7)
print(n1 > 6 or minimo == 7)
print( n1 > 6 and n2 < 10)
