# Aula 151 - Desafio 28 - Função dentro de Função
'''

Crie duas funções. A primeira deve aceitar um número e retornar o dobro desse número.
A segunda deve aceitar um número e retornar o quadrado esse número. Em seguida, chame a
primeira função dentro da segunda para retornar o quadrado do dobro de um número.

'''

def dobro(num):
    return num * 2

def quadrado(num):
    return num ** 2

x = int(input('Digite um número: '))

print(f'O dobro de {x} é {dobro(x)}')
print(f'O quadrado de {x} é {quadrado(x)}')

print(f'O quadrado do dobro de {x} é {quadrado(dobro(x))}')
