from classes.Produto import Produto
from classes.Categoria import Categoria

def menu():
    print('======= Menu =======')
    print('1 - Cadastrar Produto')
    print('2 - Listar Produtos')
    print('3 - Consultar Produto')
    print('4 - Alterar Produto')
    print('5 - Excluir Produto')
    print('6 - Cadastrar Categoria')
    print('7 - Listar Categorias')
    print('8 - Consultar Categoria')
    print('9 - Alterar Categoria')
    print('10 - Excluir Categoria')
    print('0 - Sair')
    print('=====================')

opcao = 1

while opcao != 0:

    menu()
    opcao = int(input('Digite a opção desejada: '))

    match opcao:
        case 1:
            Produto.listarTodos()
            codigo = input('Digite o código do produto: ')
            nome = input('Digite o nome do produto: ')
            quantidade = int(input('Digite a quantidade do produto: '))
            valor = float(input('Digite o valor do produto: '))

            produto = Produto(codigo, nome, quantidade, valor)
            produto.inserir()

        case 2:
            print(30 * '-', 'Lista de Produtos', 30 * '-')
            Produto.listarTodos()
            print(80 * '-')
            print()
        
        case 3:
            Produto.listarTodos()
            item = int(input('Digite o item que deseja consultar: '))
            itemConsultar = Produto.consultar(item)
            print('Item selecionado:', itemConsultar['nome'])
            print()
            
        case 4:
            Produto.listarTodos()
            item = int(input('Digite o item que deseja alterar: '))
            itemAlterar = Produto.consultar(item)
            print('Item selecionado:', itemAlterar['nome'])
            print(30 * '-', 'Digite os novos dados', 30 * '-')
            codigo = input('Digite o código do produto: ')
            nome = input('Digite o nome do produto: ')
            quantidade = int(input('Digite a quantidade do produto: '))
            valor = float(input('Digite o valor do produto: '))

            produto = Produto(codigo, nome, quantidade, valor)
            produto.alterar(item)
        
        case 5:
            Produto.listarTodos()
            item = int(input('Digite o item que deseja excluir: '))
            Produto.excluir(item)
        
        case 6:
            Categoria.listarTodos()
            nome = input('Digite o nome da categoria: ')
            categoria = Categoria(nome)
            categoria.inserir()
        
        case 7:
            print(30 * '-', 'Lista de Categorias', 30 * '-')
            Categoria.listarTodos()
            print(80 * '-')
            print()

        case 8:
            Categoria.listarTodos()
            item = int(input('Digite o item que deseja consultar: '))
            itemConsultar = Categoria.consultar(item)
            print('Item selecionado:', itemConsultar['nome'])
        
        case 9:
            Categoria.listarTodos()
            item = int(input('Digite o item que deseja alterar: '))
            itemAlterar = Categoria.consultar(item)
            print('Item selecionado:', itemAlterar['nome'])
            print(30 * '-', 'Digite os novos dados', 30 * '-')
            nome = input('Digite o nome da categoria: ')
            categoria = Categoria(nome)
            categoria.alterar(item)
            
        case 10:
            Categoria.listarTodos()
            item = int(input('Digite o item que deseja excluir: '))
            Categoria.excluir(item)
        

print()
print('Obrigado por usar o sistema!')


# Produto.excluir(0)
# item = 4
# itemAlterar = Produto.consultar(item)
# print(itemAlterar ['quantidade'])
#produto = Produto(itemAlterar['codigo'], itemAlterar['nome'], 200, 150.0)
#produto.alterar(item)
# print(produto.detalhar())
# print(Produto.consultar(0))
# Produto.listarTodos()
# Categoria.listarTodos()
# produto = Produto('006', 'Calça Jeans', 80, 299.90)
# produto.inserir()
# produto.listarTodos()
# categoria = Categoria('Eletrônicos')
# categoria.inserir()
# categoria.listarTodos()
