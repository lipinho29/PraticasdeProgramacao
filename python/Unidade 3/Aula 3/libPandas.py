import pandas as pd

cidades = [
    {'Nome': 'São Paulo', 'Estado': 'SP', 'População': 12300000},
    {'Nome': 'Rio de Janeiro', 'Estado': 'RJ', 'População': 6748000},
    {'Nome': 'Salvador', 'Estado': 'BA', 'População': 2872000},
    {'Nome': 'Brasília', 'Estado': 'DF', 'População': 3055000},
    {'Nome': 'Fortaleza', 'Estado': 'CE', 'População': 2687000},
]

dataFrame = pd.DataFrame(cidades)
# print(dataFrame)

ordenada = dataFrame.sort_values(by='População', ascending=False)
print(ordenada)
print()
print(ordenada.head(3)['Nome'])
