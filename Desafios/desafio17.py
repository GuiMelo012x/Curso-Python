# A129 - Desafio 17 - Verificador de Idade
'''

Peça ao usuário para digitar a sua idade. Se  a idade for menos que 13, imprima "Você é uma criança.".
Se a idade estiver entre 13 e 17, imprima "Você é adolescente.". Se a idade for 18 ou mais, imprima
"Você é um adulto."

BÔNUS: Trabalhar com números negativos.

'''

idade = int(input('Digite a sua idade: '))

if idade < 0:
    print('Insira uma idade válida.')
elif idade < 13:
    print('Você é uma criança.')

elif idade >= 13 and idade < 18:
    print('Você é um adolescente.')
else:
    print('Você é um adulto.')
