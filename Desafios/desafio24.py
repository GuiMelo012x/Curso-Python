# A143 - Desafio 24 - Funções Simples
'''

Crie uma função que aceita um número como entrada e retorna o quadrado deste número.

'''

x = int(input('Digite um número: '))

def quadrado(numero):
    return numero**2

print(f'{x} * {x} = {quadrado(x)}')
