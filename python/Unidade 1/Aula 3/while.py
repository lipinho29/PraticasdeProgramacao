i = 1

while i < 11:
    print(f"2 x {i} = {2 * i}")
    #i = i + 1
    i += 1
    print("-" * 20)

    continuar = input("Deseja continuar? (s/n) ")
    continuar = True if continuar == 's' else False