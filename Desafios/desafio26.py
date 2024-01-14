# A147 - Desafio 26 - Calculando Base e Expoente
'''

Crie uma função que calcule a potência de um número. A função deve aceitar dois argumentos:
a base e o expoente. No entando, se o expoente não for fornecido ao chamar a função, ele deve assumir
o valor padrão de 2.

'''


print('---- Forma 1: -----\n')
def potencia(base,expoente):
    if expoente == 0:
        expoente = 2
        print('Expoente não pode ser 0. Alterado para 2.')
    return base ** expoente

b = int(input('Digite a base: '))
e = int(input('Digite o expoente: '))

if e == 0:
    print(f'{b} elevado a {2} é {potencia(b, e)}')
else:
    print(f'{b} elevado a {e} é {potencia(b,e)}')


print('\n----- Forma 2: -----\n')

def potencia2(base2,expoente2=2):
    return base2 ** expoente2

user_number = int(input('Digite a base: '))
user_expoente = input('Digite o expoente: ')

if user_expoente:
    print(f'O resultado é: {potencia2(user_number,int(user_expoente))}')
else:
    print(f'O resultado é: {potencia2(user_number)}')












