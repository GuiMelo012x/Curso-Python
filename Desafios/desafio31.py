# A157 - Desafio 31 - Lambda com If e Else
'''

Crie uma função lambda que aceite um número e retorne "par" ou "ímpar"

'''

par_impar = lambda num: 'Par' if num%2 == 0 else 'Impar'

while True:
    x = int (input('Digite um número: '))
    if x == 0:
        break
    print(par_impar(x))



print('----- Com Função: -----')
def impar_par(num):
    if num%2 == 0:
        return 'Par'
    else:
        return 'Ímpar'
print(impar_par(1))
print(impar_par(2))

