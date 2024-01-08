print('----- Aula 48 -----')
# A48 - Listas - Criar uma lista que armazena cidades
    # Serve para manter a sequencia de dados em uma variável e armazenar mais de uma informação em variáveis

cidade1 = 'Recife'
cidade2 = 'São Paulo'
cidade3 = 'Olinda'

cidades = ['Recife', 'São Paulo', 'Olinda']
# Recife = [0] | São Paulo = [1] | Olinda = [2]
print (cidades)

print('----- Aula 49 -----')

# A49 - Manipulando Listas

cidades = ['Recife', 'São Paulo', 'Olinda']
# Recife = [0] | São Paulo = [1] | Olinda = [2]

print('Loop com While: ')
i = 0
while (3 > i):
    print(cidades[i])
    i += 1

print()

print('Loop com For: ')
cidades = ['Gramado', 'Santos', 'Caruaru']
for i in cidades:
    print(i)

print()

print(cidades)
cidades[2] = 'Garanhuns'
print(cidades) # Trocou Caruaru por Garanhuns

print('----- Aula 50 -----')

# A50 - Funções dentro de Listas - https://docs.python.org/3/tutorial/datastructures.html
# Exemplos:

#list.append - adiciona um item no final da lista.
cidades.append('Curitiba')
print(f' {cidades} - list.append - adiciona Curitiba')

#list.remove - remove um item da lista.
cidades.remove('Garanhuns')
print(f' {cidades} - list.remove - remove Garanhuns')

#list.insert - adiciona um item na posição solicitada.
cidades.insert(1, 'Porto de Galinhas') # [1] = antes de Santos, depois de Gramado.
print(f' {cidades} - list.insert - insere Porto de Galinhas')

#list.pop - remove o item da posição solicitada.
cidades.pop(0) # remove Gramado
print(f' {cidades} - list.pop - remove Gramado')

#list.sort - organiza a lista em ordem alfabética
cidades.sort()
print(f' {cidades} - list.sort - organiza em ordem alfabética' )

print('----- Aula 51 -----')

# A51 - Concatenando Listas

numeros = [1,2,3,4,5]
letras = ['a', 'b', 'c', 'd', 'e']

final = numeros * 3
print(final)

final = numeros + letras
print (final)

numeros.extend(letras)
print(f'{numeros} - list.extend - juntou 2 listas, numero com letras')

# Aqui possui duas listas em uma só.
itens = [['item1', 'item2'], ['item3', 'item4']]
#               [0]                [1]
# item1 = [0],[0] | item2 = [0],[1]
# item3 = [1],[0] | item3 = [1][1]

print(itens[0][0]) # item1
print(itens[0][1]) # item2
print(itens[1][0]) # item3
print(itens[1][1]) # item4
print(itens[0]) # item 1 e 2
print(itens[1])# item 3 e 4

print('----- Aula 52 -----')

# A52 - Extraindo Variáveis de Listas

produtos = ['arroz', 'feijão', 'laranja', 'banana','maçã','uva']

item1 = produtos[0]
print(item1)

item1, item2, item3, item4,item5,item6 = produtos
print(produtos)

item1, item2, item3, *outros = produtos # * outros - quem não foi designado

print(item1) # arroz
print(item2) # feijão
print(item3) # laranja
print(outros) # banana, maçã e uva - vai imprimir todos que nao foram designados a uma variável.

print('----- Aula 53 -----')

# A53 - Looping dentro de uma lista (já fiz acima adiantado mas farei de novo).
# Fazer um programa que diz o valor final do produto numa loja.

valores = [10,20,30,40,50]

for i in valores:
    print(f'O valor final do produto é de R$ {i}.')

print('----- Aula 54 -----')

# A54 - Verificando itens em uma lista.
# Criar um programa que verifica se uma cor está ou não em estoque.

cores = ['preto', 'branco', 'cinza', 'azul']
if 'preto' in cores:
    print('Está em estoque')
else:
    print('Fora de Estoque')

if 'amarelo' in cores:
    print('Está em estoque')
else:
    print('Fora de Estoque')


cor_cliente = input('Digite a cor desejada: ')
if cor_cliente.lower() in cores:
    print(f'{cor_cliente} está em estoque.')
else:
    print(f'{cor_cliente} está fora de estoque.')


print('----- Aula 55 -----')

# A55 - Agregando duas listas com Zip

cores = ['preto', 'branco', 'cinza', 'azul']
valores = [10,20,30,40]


var = list('comprar')
print(var)
var = list('12345')
print(var)

duas_listas = zip(cores,valores) # pode mudar a ordem também

print(list(duas_listas))

print('----- Aula 56 -----')

# A56 - Input em listas
# Criar um programa em que o usuário, através do input, faça uma lista de frutas

frutas_usuario = input('Digite o nome das frutas separados por vírgula: ')

frutas_lista = frutas_usuario.split(', ')

print(frutas_lista)


print('----- Aula 57 -----')

# A57 - Tuples
# 	A diferença entre tuples e lista, é que a tuple não pode ser alterada.

cores_lista = ['preto', 'branco', 'cinza', 'azul']
cores_tuple = ('preto', 'branco', 'cinza', 'azul') # Parênteses ao invés de colchetes

print(cores_lista)
print(cores_tuple)
# Se o conteúdo é FIXO e nunca vai ser alterado, é melhor usar tuple.
# Se o conteúdo pode ser que no futuro seja alterado, é melhor usar listas.
# Tuple é mais leve, lista gasta mais memória.

