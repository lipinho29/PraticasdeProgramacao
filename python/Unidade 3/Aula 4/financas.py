import pandas as pd
import matplotlib.pyplot as plt

class Investimento:
    def __init__(self, nome, valor, taxa, periodo):
        self.nome = nome
        self.valor = valor
        self.taxa = taxa
        self.periodo = periodo

investimentos = {
    'Investimento 1': Investimento('Poupança', 8000, 0.005, 120),
    'Investimento 2': Investimento('CDB', 5000, 0.007, 84),
    'Investimento 3': Investimento('Tesouro Direto', 11000, 0.006, 60),
    'Investimento 4': Investimento('Ações', 5000, 0.01, 36)
}

l_investimentos = [i.__dict__ for i in investimentos.values()]

df_investimentos = pd.DataFrame.from_records(l_investimentos, index=investimentos.keys())

df_investimentos['Retorno'] = df_investimentos.apply(lambda l: l.valor * (1 + l.taxa) ** l.periodo, axis=1)

print(df_investimentos)

df_investimentos.plot(kind = 'bar', y='Retorno', legend = 'Nome')
plt.title('Retorno dos Investimentos')
plt.xlabel('Tipo de Investimento')
plt.ylabel('Valor Futuro (R$)')
plt.show()