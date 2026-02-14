import matplotlib.pyplot as plt

class Campanha:
    def __init__(self, canal, investimento, cliques, conversoes):
        self.canal = canal
        self.investimento = investimento
        self.cliques = cliques
        self.conversoes = conversoes

    def cpc(self):
        return self.investimento / self.cliques 
    
campanhas = [
    Campanha("Facebook", 1500, 1200, 300),
    Campanha("Google", 2000, 1800, 400),
    Campanha("Instagram", 1000, 900, 200),
    Campanha("LinkedIn", 800, 600, 150),
]

canais = [c.canal for c in campanhas]
cpcs = [c.cpc() for c in campanhas]

plt.bar(canais, cpcs, color=['blue', 'yellow', 'pink', 'cyan'])
plt.title("CPC por Canal de Marketing")
plt.xlabel("Canal")
plt.ylabel("CPC (Custo por Clique)")
plt.show()