# A123 - Desafio 14 - Loop com Break e Continue
'''

Criar um loop que imprima os números de 1 a 10, mas pare de imprimir assim que chegar a 5 usando
o comando "break". Em seguida, criar um segundo loop que imprima os números de 1 a 10, mas pule
a impressão do 5 usando o comando "continue"

'''

print('----- Loop 1 -----')

for i in range(1,10):
    if i == 5:
        print('O i é igual a 5, fim do loop 1.')
        break
    print(i)

print('\n----- Loop 2 -----')

for i in range (1,11):
    if i==5:
        print('Pular')
        continue
    print(i)
