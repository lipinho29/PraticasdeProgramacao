import data

class Categoria:
    def __init__(self, tipo = ''):
        self.tipo = tipo

    def taxaAgua(self, consumo):

        print("Data da leitura:", data.formatarData())

        match self.tipo:
            case 'Clínica': return consumo * 1
            case 'Restaurante': return consumo * 2
            case 'Hotel': return consumo * 2.5
        

class Imovel:

    imposto = 0.2 # Atributo de classe

    def __init__(self, nome, quartos, suites):
        self.nome = nome
        self.quartos = quartos
        self.suites = suites
        self.categoria = Categoria()
    
    def __add__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf + somaOther
    
    def __gt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf > somaOther
    
    def __lt__(self, other):
        somaSelf = self.quartos + self.suites
        somaOther = other.quartos + other.suites
        return somaSelf < somaOther
    
    def __str__(self):
        #return f'Imóvel: {self.nome} - Quartos: {self.quartos} - Suítes: {self.suites}'
        return str(self.__dict__)
    
    def detalhar(self):
        return self.__dict__
    
    def somarAposentos(self):
        return self.quartos + self.suites
    
    @staticmethod
    def metodoEstatico():
        print('Chamou o método estático sem criar um objeto')

    @classmethod
    def metodoClasse(cls):
        print('Chammou o método de classe que vê o imposto', cls.imposto)
    
casarao = Imovel('Casarão', 3, 4)
# print(casarao.__dict__)

mansao = Imovel('Mansão', 4, 5)
# print(mansao.__dict__)

categoria = Categoria('Hotel')
hotel = Imovel('Hotel do Chico', 0, 150)
hotel.categoria = categoria
print(hotel.categoria.taxaAgua(500))

# print(casarao.somarAposentos())
# print(mansao.somarAposentos())

# casarao.metodoEstatico()

# print(casarao.__dict__ )

# Imovel.metodoEstatico()
# Imovel.metodoClasse()


# quartosCasarao = casarao.quartos + casarao.suites
# quartosMansao = mansao.quartos + mansao.suites
# print(quartosCasarao)
# print(quartosMansao)

soma = casarao + mansao
# print(soma)
# print (casarao > mansao) # Vai comparar o id dos objetos
# print (casarao < mansao)

# print(casarao)