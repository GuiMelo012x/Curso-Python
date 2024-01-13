# A111 - Desafio 8 - Alterando Listas
'''

Utilizando a lista frutas do desafio anterior, altere o segundo elemento da lista de "banana"
para "morango". Depois, adicione a fruta "abacaxi" ao final da lista e imprima.

'''

frutas = ['maçã','banana','manga','uva']

frutas[1] = 'morango'
frutas.append('abacaxi')
frutas.insert(4, 'abacate')

for i in frutas:
    print(i)