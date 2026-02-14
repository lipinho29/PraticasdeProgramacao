from moedas import converterCotacao

def menu():
    print("Conversor de Moedas")
    print("1. Converter Moeda")
    print("2. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        origem = input("Digite a moeda de origem (ex: USD): ").upper()
        destino = input("Digite a moeda de destino (ex: BRL): ").upper()
        valor = float(input("Digite o valor a ser convertido: "))

        resultado = converterCotacao(origem, destino, valor)
        print(f"{valor} {origem} é igual a {resultado} {destino}")

    elif escolha == '2':
        print("Saindo...")
    else:
        print("Opção inválida. Tente novamente.")
    
opcao = 1

while opcao != 0:
    menu()
    opcao = int(input("Digite 0 para sair ou qualquer outro número para continuar: "))