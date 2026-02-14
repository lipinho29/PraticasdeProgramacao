# A partir da declaração acima, width = 10 e 10 é int, então esperamos que a função retorne int
type(width)

type(helloMessage)

type(bool_Condition)

# Vamos computar um float em um int e vice-versa
# Computaremos o tipo e depois o armazenaremos em uma nova variável
width_float = float(width)

type(width_float)

# Computar entre string e int
# Lembrar que width armazena um int

# Converter width para string
width_string = str(width)
type(width_string)

# Converter width_string de volta a um int
type(int(width_string))