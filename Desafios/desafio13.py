# A121 - Desafio 13 - While Loop
'''

Utilize um while para imprimir os números de 1 a 10

'''

i = int(input('É para contar até quanto? '))
def contar(i):
    j = 0
    while j < i:
        j += 1
        print(j)


contar(i)
