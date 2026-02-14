def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
print(fatorial(6))

'''
def calcular(n1):
    return calcular (n1 - 1)

print(calcular(78))

10! = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 3628800
'''
