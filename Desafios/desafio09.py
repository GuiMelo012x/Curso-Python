# A113 - Desafio 9 - Removendo itens da Lista
'''

Utilizando a lista "frutas", remova a "manga" da lista utilizando o método remove().
Depois, remova o último item da lista usando o comando del, e depois imprima.

'''

frutas = ['maçã','morango','manga','uva','abacaxi']

frutas.remove('manga') # remove a manga
frutas.__delitem__(3) # remove o abacaxi
del frutas [0] # remove a maçã

for i in frutas:
    print(i)
