# Considere um programa que ecoe o input do usuário, exceto pelo "end".
# Este programa roda infinitamente, exceto quando o usuário insere "end" para terminá-lo.

while True:
  user = input("Enter something to be repeated: ")

  ## Quando o "break" é acionado, o print() abaixo NÃO será executado.
  ## O programa romperá o loop quando esta palavra-chave for lida.
  if user=="end":
    print("Terminate the program!!!")
    break
  print(user)

# Sem usar a palavra-chave "break", esta é outra implementação do mesmo programa de cima usando uma variável.

end = False
while end == False:
  user = input("Enter something to be repeated: ")
  if user=="end":
    print("Program Ended!!!")
    end = True
  else:
    print(user)

"""
Vamos considerar um loop que conta de 1-20, mas ignora todos os números que são múltiplos de 5. 
Neste caso, NÃO poderíamos usar a palavra-chave "break", porque isso encerrará o loop. 
Queremos "continuar" o loop, exceto por alguns números. 

Vamos implementar isto tanto com um loop "while" quanto com um loop "for". 
"""

count = 1

# Implementação do loop WHILE
while count + 1 <= 20:
  if count % 5 == 0:
    print("SKIP")
    count += 1
    continue
  print(count)
  count += 1

# Implementação do loop FOR 

for i in range (1, 20):
  if i % 5 == 0:
    print("SKIP")
    continue
  print(i)