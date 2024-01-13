# A107 - Desafio 6 - Listas
'''

Crie uma lista chamada "frutas", que contenha os itens "maçã","banana","manga" e "uva".
Depois, imprima esta lista na tela:

'''

frutas = ['maçã','banana','manga','uva']
print(frutas)

print('Com colchetes: ')
for i in frutas:
    print([i]) # para imprimir com colchetes, basta colocar o [i] junto com os colchetes.

print('Sem colchetes:')

for i in frutas:
    print(i) # para imprimir sem colchetes, basta colocar apenas o i.