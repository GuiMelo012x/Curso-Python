# A137 - Desafio 21 - Tuple de Cidades
'''

Crie uma lista com os nomes de três cidades. Peça ao usuário para digitar o nome de uma cidade.
Se a cidade estiver na lista, imprima "A cidade está na lista". Caso contrário, imprima
"A cidade não está na lista."

Obs: Não pode usar list[]
'''

cidades = ('Recife','Santos','Olinda')

while True:
    usuario = input('Digite o nome da cidade: ')
    if usuario in cidades:
        print('A cidade está na lista.')
        break
    else:
        print('A cidade não está na lista.')
