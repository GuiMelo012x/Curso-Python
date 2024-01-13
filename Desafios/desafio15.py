# A125 - Desafio 15 - Contador de Lista
'''

Criar uma lista de frutas que inclui "maçã" três vezes e outras frutas de sua escolha.
Use um for loop para contar quantas vezes "maçã" aparece na lista e imprima o resultado.

'''

frutas = ['maçã','maçã','maçã','uva','maca','melancia','banana','maça','morango','maçã']

j = 0          # contador
for i in frutas:
    if i == 'maçã':
        j += 1

print('O número de maçãs na lista é', j)
