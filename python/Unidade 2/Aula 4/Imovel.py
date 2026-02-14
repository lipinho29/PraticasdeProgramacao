from abc import ABC, abstractmethod

class Imovel(ABC):
    def __init__(self, nome, uf, valor, endereco = '', area = ''):
        self.nome = nome
        self.uf = uf
        self.valor = valor 
        self.endereco = endereco
        self.area = area
    
    def detalhar(self):
        print(self.__dict__)

    def calcularImposto(self):
        return self.valor * 0.03
    
    @abstractmethod
    def aluguelSugerido(self):
        pass
    
class ImovelResidencial(Imovel):
    def __init__(self, nome, uf, valor, endereco= '', area= ''):
        super().__init__(nome, uf, valor, endereco= '', area= '')
        self.quartos = 3
        self.piscina = False

    def aluguelSugerido(self):
        return self.valor * 0.01

class ImovelComercial(Imovel):
    
    def aluguelSugerido(self):
        return self.valor * 0.015

class ImovelRural:
    def __init__(self, hectares = '', curral = '', produtivade = True):
        self.hectares = hectares
        self.curral = curral
        self.produtivade = produtivade
    
    def mesPlantacao(self, mes):
        match int(mes):
            case 1: return 'Janeiro - Plantação de soja'
            case 2: return 'Fevereiro - Plantação de milho'
            case 3: return 'Março - Plantação de feijão'
            case 4: return 'Abril - Plantação de arroz'
            case 5: return 'Maio - Plantação de trigo'
            case 6: return 'Junho - Plantação de café'
            case 7: return 'Julho - Plantação de cana-de-açúcar'
            case 8: return 'Agosto - Plantação de algodão'
            case 9: return 'Setembro - Plantação de laranja'
            case 10: return 'Outubro - Plantação de uva'
            case 11: return 'Novembro - Plantação de maçã'
            case 12: return 'Dezembro - Plantação de pêssego'

class Fazenda(Imovel, ImovelRural):
    def aluguelSugerido(self):
        return self.valor * 0.025


print('*' * 125)
fazenda = Fazenda('Fazenda Boa Vista', 'MT', 2500000, 'Estrada Rural, s/n', '1500m2')
fazenda.detalhar()
print(f'Imposto da fazenda: R$ {fazenda.calcularImposto()}')
print(f'Aluguel sugerido da fazenda: R$ {fazenda.aluguelSugerido()}')
print(f'Mês e plantação eficaz: {fazenda.mesPlantacao(1)}')
print()
print('*' * 125)


casa = ImovelResidencial('Minha Casa', 'MG', 500000, 'Rua B, 456', '120m2')
casa.detalhar()
print(f'Imposto da casa: R$ {casa.calcularImposto()}')
print(f'Aluguel sugerido da casa: R$ {casa.aluguelSugerido()}')
print()
print('*' * 125)

clinica = ImovelComercial('Clínica Médica', 'RJ', 1200000, 'Av. C, 789', '300m2')
clinica.detalhar()
print(f'Imposto da clinica: R$ {clinica.calcularImposto()}')
print(f'Aluguel sugerido da clinica: R$ {clinica.aluguelSugerido()}')
print()
print('*' * 125)

'''    
imovel0 = Imovel('Apartamento', 'SP', 350000, 'Rua A, 123', '75m2')
imovel0.detalhar()
'''