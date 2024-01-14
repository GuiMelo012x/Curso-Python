# A133 - Desafio 19 - Encontrando um item com While.
'''

Crie um loop que peça ao usuário para digitar o nome de uma fruta. Se a fruta digitada não for
"abacate", o loop deve continuar pedindo ao usuário para digitar o nome da fruta. Se a fruta for
"abacate", o loop termina e o programa imprime "Parabéns, você acertou a fruta!".

'''

print('----- Forma 1: -----')
print('Fase 1: \n')
fruta = input('Digite uma fruta: ')

while fruta.lower() != 'abacate':
    fruta = input('Errou! Digite novamente: ')


print('Parabéns, você acertou a fruta!\n')

print('----- Forma 2: -----')


print('Fase 2: \n')
while True:
    fruta2 = input('Digite uma fruta: ')
    if fruta2.lower() == 'morango':
        break

print('Você acertou a fruta!')
