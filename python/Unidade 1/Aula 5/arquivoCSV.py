import csv

carros = [
    {"Ford", "Fiesta", 2020},
    {"Chevrolet", "Onix", 2021},
    {"Volkswagen", "Gol", 2019},
    {"Fiat", "Palio", 2018},
]

with open('carros.csv', 'w', newline='') as arquivo:
    filecsv = csv.writer(arquivo, delimiter=',')

    filecsv.writerow(["marca", "modelo", "ano"])  # Cabeçalho
    filecsv.writerows(carros)  # Dados