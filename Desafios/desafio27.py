# A149 - Desafio 27 - Calculando Fatorial
'''

As funções recursivas são funções que se chamam dentro do seu próprio bloco de código. Elas são
úteis para resolver problemas que podem ser divididos em problemas menores de natureza semelhante.

Um exemplo clássico de onde a recursão é usada é o cálculo do fatorial de um número. O fatorial de um
número n é o produto de todos os números inteiros positivos de n até 1.

'''
import math


def fatorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return math.factorial(num)

x = int(input('Digite um número para fazer o fatorial: '))
print(f'O fatorial de {x} é {fatorial(x)} ')
