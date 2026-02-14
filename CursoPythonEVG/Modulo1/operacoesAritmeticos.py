# Operações matemáticas básicas com Números

# Adição
print(5+23)

# Subtração
print(100-25)

# Multiplicação
print(5*10)

# Potência/Exponente
# o operador ** é equivalente ao expoente
print(5**2)

# 5*5 = 5^2 = 5**2 
print(5*5)


# Divisão (float)
# Retornar o valor decimal real da divisão
print(36/4)
print(10/3)         

# Divisão (int)
# Retornar um int. Se o quociente real for um valor decimal, apenas um número inteiro irá retornar
print(10//3)
print(19//6)

# Divisão Modular: retornar o restante da divisão
print(10%3)

# Operações com Strings e Caracteres
print("foo" * 5)
print('x'*3)

# ERRO: o compilador trata x como uma variável, não como um caractere
print(x*3)

# ERRO: não pode concatenar um int com uma string --> necessidade de computar int com uma string
print("hello" + 5)

# Fix
print("hello " + str(5))

# Adição de String = concatenação
print("hello " + "world")