arquivo = open('pessoas3.txt', 'w')

arquivo.write('Joao\n')
arquivo.write('Maria\n')
arquivo.write('Pedro\n')

arquivo.close()

with open('pessoas3.txt', 'r+') as arquivoleitura:
    for linha in arquivoleitura:
        print(linha)
