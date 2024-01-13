# A103 - Desafio 04 - Input.
'''

Crie um script que pergunta o nome e a idade do usuário, usando a função input. Depois disso,
o script deve imprimir uma mensagem dizendo "Olá, [nome]! Você tem [idade] anos".

'''

def cadastro():
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    return print(f'Olá, {nome}! Você tem {idade} anos!')

cadastro()