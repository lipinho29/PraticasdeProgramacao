import matplotlib.pyplot as plt
from moedas import get_cotacao

def grafico_barra(l_moedas, l_valores):
    plt.bar(l_moedas, l_valores, color=['red', 'blue', 'green'])
    plt.title('Cotação Atual das Moedas em Relação ao Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('Valor em BRL')
    plt.show()

def grafico_pizza(l_moedas, l_valores):
    plt.pie(l_valores, labels=l_moedas)
    plt.title('Proporção das Moedas em Relação ao Real (BRL)')
    plt.show()

def grafico_dispersao(l_moedas, l_valores):
    plt.scatter(l_moedas, l_valores, color='purple')
    plt.title('Cotação Atual das Moedas em Relação ao Real (BRL)')
    plt.xlabel('Moedas')
    plt.ylabel('Valor em BRL')
    plt.show()

