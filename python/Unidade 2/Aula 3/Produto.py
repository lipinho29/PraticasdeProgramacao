class Produto:
    
    def __init__(self, nome = '', marca = '', modelo ='', valor = 0.0, quantidade = 0):
        self.nome = nome
        self.marca = marca
        self.modelo = modelo
        self.valor = valor
        self.quantidade = quantidade

    def vender(self, quantidade):
        if quantidade > self.quantidade:
            print()
            print('**'*20)
            print('Não há estoque suficiente')
            print(f'Estoque atual: {self.quantidade}')
            print('**'*20)
            print()
        else:
            self.quantidade -= quantidade

    def comprar(self, quantidade):
        self.quantidade += quantidade

produto0 = Produto('Caneta', 'Bic', 'Azul', 1.50, 100)
#produto0.nome = "Caneta"
#produto0.marca = "Bic"
#produto0.modelo = "Azul"
#produto0.valor = 1.50
#produto0.quantidade = 100
produto0.comprar(10)
produto0.vender(110)

produto1 = Produto('Lápis', 'Faber-Castell', 'HB', 0.50, 200)

produto2 = Produto('Caderno', 'Tilibra', '100 folhas', 12.00, 150)
produto2.comprar(50)
produto2.vender(20)

produto3 = Produto()

print(produto0.__dict__)
print(produto1.__dict__)
print(produto2.__dict__)
print(produto3.__dict__)