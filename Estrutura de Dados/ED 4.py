from sys import getsizeof

print('----- Aula 66 -----')
# A66 - Função Lambda
    # É uma função pequena e sem nome, podendo ter vários argumentos, mas somente uma expressão.
    # É muito utilizada dentro de outras funções, e deixa o código mais limpo.

def somar(x):
    return x + 10

print(f'Função somar - {somar(2)}')

#argumento: x | lambda: x+10

somar10 = lambda x: x+10

print(f'Modo Lambda - {somar10(2)}')

somar2N = lambda x,y: x + y + 10

print(somar2N(2,4)) # 16

print('----- Aula 67 -----')

# A67 - Lambda dentro de uma função

def somar(x):
    funcao2 = lambda x: x + 10
    return funcao2(x) * 4

print(somar(2))

print('----- Aula 68 -----')

# A68 - Função Map em uma Lista
    # Muito utilizado em listas, e aplica uma função a um iterable, por item. (list, tuple, dicionário, etc.)
    # Criar um programa que multiplica os valores da lista [1,2,3,4] por 2
    # Resultado desejado = [2,4,6,8]

lista1 = [1,2,3,4]

def multi(x):
    return x * 2


lista2 = map(multi,lista1)

print(list(lista2)) # --> [2,4,6,8]


print('----- Aula 69 -----')

# A69 - Função Map com lambda
# Criar um programa que transforme estas 6 linhas de código em apenas uma
'''
lista1 = [1,2,3,4]
def multi(x):
    return x * 2

lista2 = map(multi,lista1)
print(list(lista2)) # --> [2,4,6,8]
'''

# lista2 = map(lambda x: x*2,lista1)
print(list(map(lambda x: x*2,lista1)))

print('----- Aula 70 -----')

# A70 - Função Filter
# Criar um programa que filtre valores abaixo de 20

valores = [10,12,34,44,57]

def remover20(x):
    return x>20

print(list(filter(remover20,valores))) # com função

print(list(filter(lambda x: x>20,valores))) # com lambda


print('----- Aula 71 -----')

# A71 - List Comprehension com String
# Forma mais facil de escrever, utilizado quando voce precisa criar uma nova lista a partir de outra existente.
# [expressao for iten in itens]
# Fazer um programa que jogue em outra lista as frutas que contém a letra "B"

frutas1 = ['abacate','banana','morango','kiwi','abacaxi']
frutas2 = [] # lista vazia
frutas3 = [] # lista vazia

for letras in frutas1:
    if 'b' in letras:
        frutas2.append(letras) # adiciona as frutas com b na lista 2, que deram true no IF
    else:
        frutas3.append(letras) # adiciona as frutas sem b na lista 2, que não deram false no IF


print(frutas1)
print(frutas2)
print(frutas3)
print()
# Agora, fazer tudo isto novamente em apenas 1 linha de código:
# [expressão for item in item]
# neste caso, [expressão for item in item condicao]

frutas4 = [letra for letra in frutas1 if 'b' in letra]
print(frutas4)

print('----- Aula 72 -----')

# A72 - List Comprehension com Números
# Fazer um programa que some 10 em 10 a cada index.

numeros = []
for x in range(6):
    numeros.append(x * 10)

print(numeros)

# Agora, tudo isto em apenas uma linha de código:
# [expressão for item in item]
novaLista = [x*10 for x in range(6)]
print(novaLista)

print('----- Aula 73 -----')

# A73 - Lista e Generator Expressions
# Uma forma mais rápida para listas, dicionários e etc.
# Menos memória alocada.
# Valores em bytes.
# Para usar, só trocar o colchetes pelos parênteses.


#  Para checar quanto está gastando de memória, deve-se importar a função --> from sys import getsizeof (linha1)
numeros2 = [x*10 for x in range(50)]
numeros3 = (x*10 for x in range(50))

print(list(numeros2))
print(getsizeof(numeros2)) # 472 bytes com a lista.

print(list(numeros3))
print(getsizeof(numeros3)) # 200 bytes com o generator.











