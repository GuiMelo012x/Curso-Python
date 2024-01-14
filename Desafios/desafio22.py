# A139 - Desafio 22 - Pesquisa de País e Capital
'''

Crie uma lista com 5 nomes de países e suas capitais. Peça ao usuário para digitar o nome de um país.
Se o país estiver na lista, imprima "A capital de [país] é [capital]". Se o país não estiver na lista,
imprima "Desculpe, não temos informações sobre a capital desse país.".

'''

capitais = {
    'Brasil': 'Brasília',
    'Estados Unidos':'Washington D.C',
    'França': 'Paris',
    'Itália': 'Roma',
    'Irlanda': 'Dublin'
}

usuario = input('Digite o país: ')
if usuario in capitais:
    print(f'A capital de {usuario} é {capitais[usuario]}')
else:
    print('Desculpe, não temos informações sobre a capital desse país.')
