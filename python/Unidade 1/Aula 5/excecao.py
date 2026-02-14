'''
try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    resultado = n1 / n2

    print(f"O resultado da divisão é: {resultado}")

except Exception as erro:
    print(f"Ocorreu um erro: {erro}")
'''

novadivisao = True
while novadivisao:

    try:
        n1 = int(input("Digite o primeiro número: "))
        n2 = int(input("Digite o segundo número: "))

        resultado = n1 / n2

        print(f"O resultado da divisão é: {resultado}")

    except ValueError:
        print("Por favor, digite apenas números inteiros.")

    except ZeroDivisionError:
        print("Não é possível dividir por zero.")

    except Exception as erro:
        print(f"Ocorreu um erro inesperado: {erro}")

    else:
        print("A divisão foi realizada com sucesso!")
    
    finally:
        print("Fim da operação de divisão.")

    novadivisao = input("Deseja realizar uma nova divisão? (s/n) ")
    novadivisao = True if novadivisao == 's' else False

    if not novadivisao:
        print("Encerrando o programa.")

