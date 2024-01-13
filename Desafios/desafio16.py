# A127 - Desafio 16 - Verificador de Números com If e Else
'''

Peça ao usuário que digite um número, se ele for maior que 10, imprima "o número é maior que 10",
se for menor, imprima "o número é menor que 10".

Bônus: diga se um número é impar ou par. (implementado por mim mesmo)

'''

n = int(input('Digite o número: '))

if n > 10:
    print(f'O número {n} é maior do que 10.')
elif n < 10:
    print(f'O número {n} é menor do que 10.')
else:
    print('O número é igual a 10.')



if n%2 == 0:
    print(f'O número {n} é par.')
else:
    print(f'O número {n} é ímpar.')
