n1 = 10
n2 = 4
n3 = 6
n4 = 2

soma = n1 + n2 + n3 + n4
media = soma / 4

print("Soma das quatro notas é:", soma)
print("Média do aluno é:", media)

if media >= 7:
    print("Aluno aprovado!")
elif media < 5:
    print("Aluno reprovado!")
else:
    print("Aluno em recuperação!")
