"""
    Um livro da biblioteca.
    """
class LibraryBook (object):   

      """
      O parâmetro self é OBRIGATÓRIO dentro da classe, 
      porque ele diz ao programa para buscar/atuar sobre o objeto de instância
      que a executou.
      """  
      def __init__(self, title, author, pub_year, call_no):
          self.title = title
          self.author = author
          self.year = pub_year
          self.call_number = call_no
          self.checked_out = False

"""
Como já criamos meu_livro como um objeto do LibraryBook,
agora podemos adicionar manualmente o título, autor,... informações associadas ao livro.
"""

my_book.title = "Harry Potter and the Philosopher's Stone"
my_book.author = ('Rowling', 'J.K.')
my_book.year = 1998
my_book.call_number = "PZ7.R79835"

# Busque um campo de dados específico de uma instância executando o nome da instância e o nome do campo
my_book.author

"""
Ou podemos passar todas as informações para o __init__ para configurar os campos 
ao criar a nova instância.
"""

new_book = LibraryBook("Harry Potter and the Sorcerer's Stone", 
                       ("Rowling","J.K."), 1998, "PZ7.R79835")

new_book.author