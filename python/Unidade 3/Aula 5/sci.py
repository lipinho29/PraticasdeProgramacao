from sklearn.cluster import KMeans
import numpy as np

class Produto:
    def __init__(self, nome, preco, peso):
        self.nome = nome
        self.preco = preco
        self.peso = peso

produtos = [
    Produto("Produto A", 10, 1.5),
    Produto("Produto B", 20, 2.0),
    Produto("Produto C", 15, 1.0),
    Produto("Produto D", 30, 3.0),
    Produto("Produto E", 25, 2.5),
    Produto("Produto F", 5, 0.5),
]

precos = [[p.preco, p.peso] for p in produtos]
matriz = np.array(precos)

kmeans = KMeans(n_init='auto', n_clusters=2, random_state=0).fit(matriz)
labels = kmeans.labels_

for i in range(2):
    print(f"Grupo {i+1}:")
    for j in range(len(produtos)):
        if labels[j] == i:
            print(f" - {produtos[j].nome} (Preço: {produtos[j].preco}, Peso: {produtos[j].peso})")