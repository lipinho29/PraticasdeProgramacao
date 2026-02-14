# Inicializar uma tupla vazia
y = tuple()
y

# Criar uma nova tupla de elementos
x = (1,2,3)

# ERROR: não pode ser adicionado a uma tupla
x.append(4)

# Isto é OK porque está criando uma nova tupla com x e (4,5,6) adicionado no final
x + (4,5,6)

# x NÃO é modificado pela linha anterior
x

# Criar uma nova tupla com x aparecendo duas vezes
x * 2

# Index dos elementos na tupla
x.index(3)

# abreviação para 
#  (a,b,c) = (1,2,3)

# Isto também atribui a = 1, b = 2, c = 3

a,b,c = 1,2,3

a

b

c

# Converter uma tupla em uma lista
x = (1,2,3,4)
list(x)

# Converter uma lista em uma tupla
x = [1,2,3,4]
tuple(x)

# Declarar uma nova tupla, nome "person"
person  = ('Jane','Doe', 21)

# "Pacote"/associar cada elemento da tupla com uma etiqueta. Observe a ordem das etiquetas.
first, last, age = person

first

last

age

# ERROR: x é uma tupla de 4 valores, mas está tentando descompactar SOMENTE 3 elementos.
# Incompatibilidade no tamanho da tupla
x = (1,2,3,4)

a,b,c = x

# Isto é OK!
x = [1,2,3,4]
a,b,c,d = x

a

b

c

d
