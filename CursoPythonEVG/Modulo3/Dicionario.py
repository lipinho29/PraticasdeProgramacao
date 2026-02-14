# Inicializar um dicionário vazio
# O mesmo do conjunto, mas com:
dict = {}

# Declare um dicionário com pares de chaves/valores
dict2 = {'a': 5, 'b': 10, 'c': 100, 'd': 9.5}

# Acessar dados em um dicionário com uma chave
dict2['b']

# Atualização do valor de uma chave existente
dict2['b'] = 50

dict2['b']

# O que acontece se quisermos ter acesso ao valor de uma chave inexistente? (por exemplo, 'z')


# Podemos esperar um ERROR porque esta chave não existe, portanto, não tem valor. 
# Esta é uma suposição correta.
dict2['z']

# # Mas se fizermos isso, será que isso ainda retornará um ERROR?
dict2['z'] = 999

dict2['z']

# Os valores no dicionário podem ser misturados
# Vejamos um exemplo com dict{}, um dicionário vazio iniciado acima.
# Primeiro, vamos inserir alguns pares de chaves/valores no programa. 

dict["greeting"] = "hello message"
dict["alphabet"] = ['a', 'b', 'c', 'd', 'e']
dict["check-in"] = False
dict["phoneNumber"] = 8007782346

dict

# Nota IMPORTANTE: a chave deve ser um objeto imutável (algo que não pode ser modificado)
# A string é imutável, porque você não poderia simplesmente apagar um caractere em uma string. Uma string é uma string, do jeito que ela é.

# Vemos acima que uma lista pode ser um valor no dicionário. 
# O que acontece quando tentamos fazer dela uma chave?

# ERROR: tipo inalcançável de lista 

# Porque poderíamos modificar a lista inserindo novos elementos, ordenando elementos, apagando elementos ou outras formas de modificá-la, mas ela NÃO PODE ser uma chave


dict[['a','b', 'c']] = [False, True, False]

# Mas como a tupla é imutável, podemos substituir a lista por uma tupla
dict[('a','b', 'c')] = [False, True, False]

dict

# Podemos também buscar todas as chaves
dict.keys()

# Ou todos os valores
dict.values()

# Os elementos de um dicionário também podem retornar como um par.
dict.items()

