"""
Escreveremos nossa própria função que testa se um triângulo de 3 lados é um triângulo retângulo. 
Como não podemos controlar a ordem dos lados que o usuário nos dá (de tal forma que C é o comprimento mais longo), 
precisamos verificar manualmente se C é o comprimento mais longo (os comprimentos A e B podem estar em qualquer ordem). 
Caso contrário, nosso teorema de Pitágoras falhará. 
"""

def isRightTriangle(a, b, c):

  # Reatribuir valores variáveis para garantir que C seja o comprimento mais longo
  if (max(a,b,c) != c):

    # tmp armazena os valores anteriores de C, que não é o comprimento mais longo
    tmp = c
    c = max(a,b,c)

    if a == c:
      a = tmp
    elif b == c:
      b = tmp
    

  # Aplicar a fórmula
  if a**2 + b**2 == c**2:
    print("Right Triangle")

    # Se o programa vê uma declaração Return, este é o FIM do programa/função
    return True
  
  # Estas duas linhas funcionarão SOMENTE quando a condição IF for falsa
  print("NOT a right triangle")
  return False


# Solicite ao usuário que insira 3 comprimentos
def main():
  a = input("Enter the length for the first edge of the triangle:")
  b = input("Enter the length for the second edge of the triangle:")
  c = input("Enter the length for the last edge of the triangle:")

  # As entradas do usuário são armazenadas como uma string, então nós as computamos para ser int
  return isRightTriangle(int(a), int(b), int(c))

if __name__ == "__main__":
    main()

"""
Outro exemplo: determinar se a entrada do usuário é um palíndromo. 

Palíndromo: se uma palavra/sentença é soletrada da mesma maneira quando é invertida. 
  EX: racecar (carro de corrida)

Para este exemplo, vamos tornar isto de forma mais abrangente. 
Em vez de verificar se uma palavra é um palíndromo, vamos testar se uma frase é um palíndromo. 

A fim de escrever este programa, estabeleceremos algumas especificações:
  - Tratar as letras maiúsculas como minúsculas
  - Ignorar todos os espaços brancos e pontuações
  - Uma sentença/string vazia é considerada como um palíndromo. 
"""

# importar o pacote de string
# Revisaremos mais pacotes/bibliotecas no Módulo 5
import string


# Esta implementação da função RETURN (retornar) um valor booleano, True/False (Verdadeiro/Falso)
def isPalindrome(str):

    # Como não conseguimos controlar o que o usuário insere na sentença, vamos esclarecer primeiro a sentença.
    # Vamos remover todas as pontuações e espaços brancos da sentença e colocar todas as letras em minúsculo 
    exclude = set(string.punctuation)
    str = ''.join(ch for ch in str if ch not in exclude)
    str = str.replace(" ", "").lower()

    # Comparar a string original com a string em ordem inversa
    # Observação de str[::-1]: os dois primeiros números definem o início e o fim da string, o último número de -1 indica a ordem inversa

    # Verificar se a string é a mesma tanto em ordem invertida quanto na ordem original
    if str == str[::-1]:
        return True
    else:
        return False

# Solicitar ao usuário que introduza a sentença
def main():
  userSentence = input("Enter a sentence to be tested as a palindrome:")

  if (isPalindrome(userSentence)):
    print(userSentence + " is a palindrome!")
  else:
    print(userSentence + " is NOT a palindrome!")

if __name__ == "__main__":
    main()

# Considere esta implementação da função que RETURN (retorna) uma string.
# Anote a diferença entre main() e isPalindrom() após esta mudança. 

import string

def isPalindrome(str):
  exclude = set(string.punctuation)
  str = ''.join(ch for ch in str if ch not in exclude)
  str = str.replace(" ", "").lower()
  if str == str[::-1]:
    return str + " is a palindrome!"
  else:
    return str + " is NOT a palindrome!"

def main():
  userSentence = input("Enter a sentence to be tested as a palindrome:")
  print(isPalindrome(userSentence))

if __name__ == "__main__":
    main()

