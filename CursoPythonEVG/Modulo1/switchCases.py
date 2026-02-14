def switcher(number):

  # Use dicionário (do Módulo 3) para armazenar switch cases
  # Se não for encontrado, o get() será o valor padrão
  return {
    '0':"Entered 0",
    '1':"Entered 1",
    '2':"Entered 2",
    '3':"Entered 3",
    '4':"Entered 4",
    '5':"Entered 5",
    '6':"Entered 6",
    '7':"Entered 7",
    '8':"Entered 8",
    '9':"Entered 9",
  }.get(number,"Invalid number!")


# input() lê uma entrado do usuário de stdin
number = input("Dial a number")
switcher(number)