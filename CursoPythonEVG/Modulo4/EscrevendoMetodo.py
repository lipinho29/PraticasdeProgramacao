class LibraryBook(object):
    """
    Um livro da biblioteca.
    """
         
    def __init__(self, title, author, pub_year, call_no):
        self.title = title
        self.author = author
        self.year = pub_year
        self.call_number = call_no
    
    """
    Métodos para o LibraryBook
    """  

    # Retorna o título e as informações do autor do livro como uma string
    def title_and_author(self):
        return "{} {}: {}".format(self.author[1], self.author[0], self.title) 
    
    # Imprime todas as informações associadas a um livro neste formato
    def __str__(self): # certifique-se de que __str__ retorna uma string!
        return "{} {} ({}): {}".format(self.author[1], self.author[0], self.year, self.title) 

    # Retorna uma representação de string do livro com o título e call_number     
    def __repr__(self): 
        return "<Book: {} ({})>".format(self.title, self.call_number)
    
# A simples chamada da própria instância está desencadeando __repr__()
new_book

# print está desencadeando a __string__()
print(new_book)

new_book = LibraryBook("Harry Potter and the Sorcerer's Stone", 
                       ("Rowling","J.K."), 1998, "PZ7.R79835")

new_book.title_and_author()
