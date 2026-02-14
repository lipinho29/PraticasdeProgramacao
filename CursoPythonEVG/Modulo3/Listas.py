# Iniciar uma lista vazia
list1 = []
# OU
list1 = list()

# Iniciar uma lista com elementos
list2 = ['hello', 'hola', 'olá']

"""
Os elementos da lista NÃO precisam ser do mesmo tipo, mas isto é incomum.
Neste caso, cada lista poderia representar a série de informações sobre uma pessoa, 
mas é preciso lembrar quais informações são armazenadas em cada index. ---> Existe uma opção melhor para este propósito - dicionário.
"""
list3 = ["John", "male", 20, False]

# Acess às informações armazenadas na lista por posição ("index")
# Nota: em CS, a primeira posição é SEMPRE 0
print("First element in list2 : "+ list2[0])
print("Second element in list2 : "+ list2[1])

# Inserir um novo elemento como um local específico, no index 1
list2.insert(1,'hallo')
list2[1]

# Anexar um novo elemento no FIM da lista
list2.append('bye')
list2

# Remover um elemento da lista especificando o elemento que você deseja remover
list2.remove('hello')

# list2 após o 'hello' é REMOVIDA
list2

"""
Outra maneira de remover um elemento: pop()
pop() permite que você identifique uma posição 
"""

list2.append("hello")

list2.pop()

list2

"""
As listas também podem ser ordenadas. 
O método de ordenação depende de como a interface comparável é implementada para os objetos da lista.

Neste caso da list2, sort() funciona ordenando caracteres individuais na string de acordo com o código ASCII.
"""
list2.sort()
list2

"""
Como a lista é dinâmica, significa que o tamanho da lista aumenta ou diminui à medida que inserimos ou removemos elementos,
poderíamos executar len() para encontrar o tamanho da lista em um determinado momento. 
"""

# Como len() retorna int, para concatená-la a uma string, precisamos computá-la.
print("size of list1 = " + str(len(list1)))
print("size of list2 = " + str(len(list2)))

# Imprimir itens na lista como string, separados por uma vírgula
",".join(list2)

# Você também pode ter uma lista de listas. Por exemplo:

lists = []
lists.append([1,2,3])
lists.append(['a','b','c'])

lists

# Da mesma forma, você pode indexar as listas multidimensionais.

lists[1]

lists[1][0]
