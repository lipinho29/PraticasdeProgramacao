continuar = True

while continuar:

    numero = int(input("Qual tabuada você deseja? "))

    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
        print("-" * 20)

    continuar = input("Deseja continuar? (s/n) ")
    continuar = True if continuar == 's' else False
   