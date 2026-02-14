import matplotlib.pyplot as plt

meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
qtdTI = [10, 20, 15, 25, 30, 22, 18, 27, 35, 40, 38, 45]
qtdRH = [5, 15, 10, 20, 25, 18, 12, 22, 30, 35, 33, 40]

# plt.plot(meses, qtdTI, marker='o', color='blue', label='TI', linestyle='-')
# plt.bar(meses, qtdRH, alpha=0.5)
# plt.plot(meses, qtdRH, marker='s', color='red', label='RH', linestyle='-')
# plt.title('Quantidade ao Longo dos Meses')
# plt.xlabel('Meses')
# plt.ylabel('Valores')
# plt.legend()
# plt.show()

navegadores = ['Chrome', 'Firefox', 'Edge', 'Safari', 'Opera']
qtd = [1200, 800, 600, 400, 200]
cores = ['yellow','orange', 'blue', 'gray', 'red']

plt.pie(qtd, labels=navegadores, autopct='%1.1f%%', startangle=140, colors=cores)
plt.title('Uso de Navegadores em 2023')
plt.legend()
plt.show()