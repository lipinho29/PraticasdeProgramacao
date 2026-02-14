from moedas import get_cotacao
from grafico import *
def menu ():
    print("Escolha o tipo de gráfico:")
    print("1. Gráfico de Barras")
    print("2. Gráfico de Pizza")
    print("3. Gráfico de Dispersão")
    print("0. Sair")
    
opcao = 1

cotacoes = get_cotacao()

l_moedas = ['USD - Dólar', 'EUR - Euro', 'GBP - Libra Esterlina']
l_valores = [1 / cotacoes['USD'], 1 / cotacoes['EUR'], 1 / cotacoes['GBP']]

while opcao != 0:

    menu()
    opcao = int(input("Escolha uma opção: "))

    match opcao:
        case 1: grafico_barra(l_moedas, l_valores)
        case 2: grafico_pizza(l_moedas, l_valores)
        case 3: grafico_dispersao(l_moedas, l_valores)
        case 0: print("Saindo...")
        case _: print("Opção inválida. Tente novamente.")

print()
print('Obrigado por utilizar nosso sistema!')