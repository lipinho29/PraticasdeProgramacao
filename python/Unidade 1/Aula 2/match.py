dia = int(input("Digite o número do dia da semana: "))

'''
if dia == 1:
    print("Hoje é Domingo")
elif dia == 2:
    print("Hoje é Segunda-feira")
elif dia == 3:
    print("Hoje é Terça-feira")
elif dia == 4:
    print("Hoje é Quarta-feira")
elif dia == 5:
    print("Hoje é Quinta-feira")
elif dia == 6:
    print("Hoje é Sexta-feira")
elif dia == 7:
    print("Hoje é Sábado")
else:
    print("Dia inválido")
'''

match dia:
    case 1:
        print("Hoje é Domingo")
    case 2:
        print("Hoje é Segunda-feira")
    case 3:
        print("Hoje é Terça-feira")
    case 4:
        print("Hoje é Quarta-feira")
    case 5:
        print("Hoje é Quinta-feira")    
    case 6:
        print("Hoje é Sexta-feira")
    case 7:
        print("Hoje é Sábado")
    case _:
        print("Dia inválido")