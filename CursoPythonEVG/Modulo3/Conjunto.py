# Inicializar um conjunto vazio
newSet = set()
newSet

# Um conjunto com elementos
ex1 = {1, 2, 2, 1, 1}

ex1

ex2 = {j for j in range(10)}
ex2

# 2 já existe no ex2. O que acontece se quisermos acrescentar o 2 novamente?
  # Nota: A implementação do conjunto NÃO definiu append(), então usaremos add().
    # add() irá inserir o novo elemento na posição correta com a ordenação do conjunto
ex2.add(2)
ex2.add(100)
ex2.add(50)
ex2

# objetos mutáveis não podem ser colocados em um conjunto
d_set = {[1,2,3]}

d_set

# Converter uma lista em um conjunto
ages = [10, 5, 4, 5, 2, 1, 5]

set_of_ages = set(ages)

set_of_ages

# Converter um conjunto em uma lista
list_of_ages = list(set_of_ages)

list_of_ages

# Converter um conjunto em uma tupla
tuple_of_ages = tuple(list_of_ages)

tuple_of_ages

# A ordem é irrelevante na comparação de conjuntos, uma vez que os elementos são ordenados

{1,2,3} == {2,1,3}

