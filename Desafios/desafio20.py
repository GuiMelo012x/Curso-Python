# A135 - Desafio 20 - Par e Ímpar
'''

Crie uma lista de números de 1 a 10. Use um "for" para iterar sobre a lista. Se o número atual
da iteração for par, imprima "O número [número] é par.". Se for ímpar, imprima "O número [número] é ímpar."

'''

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in lista:
    if i%2 == 0:
        print(f'O número {i} é par.')
    else:
        print(f'O número {i} é ímpar.')


print('\n----- Forma 2 ----- ')

numeros = list(range(1,11)) # forma 2 de fazer uma lista

for i in numeros:
    if i%2 == 0:
        print(f'O número {i} é par.')
    else:
        print(f'O número {i} é ímpar.')
