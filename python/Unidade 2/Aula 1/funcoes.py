def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 == 0:
        return "Erro: Divisão por zero não é permitida."
    else:
        resultado = n1/n2
        #print(f"{n1} / {n2} = {resultado}")
        return resultado

def calcular(n1, n2, operador):
    match operador:
        case '+': return somar(n1, n2)
        case '-': return subtrair(n1, n2)
        case '*': return multiplicar(n1, n2)
        case '/': return dividir(n1, n2)
        case other: return "Operador inválido"

print(calcular(5, 10, '+'))
print(calcular(5, 10, '-'))
print(calcular(5, 10, '*'))
print(calcular(5, 0, '/'))
print(calcular(5, 10, 'o'))

    
'''
print(somar(90, 789))
print(subtrair(90, 789))
print(multiplicar(90, 789))
print(dividir(90, 789))

divisao = dividir(80, 0)
print("O resultado da divisão é:", divisao)

print("Resultado", dividir(20, 4))

resultado = dividir(30, 5)

soma  = 20 + resultado
print("O resultado da soma é:", soma)

dividir(6, 3)
'''