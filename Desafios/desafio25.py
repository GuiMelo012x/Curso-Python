# A145 - Desafio 25 - Soma com Funções
'''

Crie uma função que aceite dois números como entrada e retorna a soma desses números.

'''
print('----- Forma 1: -----')
def soma (num1,num2):
    return num1 + num2

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
print(f'{x} + {y} = {soma(x,y)}')           # Melhor usar esta forma.




print('\n----- Forma 2: -----')
def soma2 (num3,num4):
    resultado = num3 + num4
    return print(f'{num3} + {num4} = {resultado}')


a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
soma2(a,b)
