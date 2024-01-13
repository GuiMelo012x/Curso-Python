# A119 - Desafio 12 - Nested for Loop
'''

Crie uma lista de frutas e outra de vegetais. Use um for loop aninhado (nested for loop) para imprimir
todas as combinações possíveis de frutas e vegetais, com a fruta primeiro e o vegetal em segundo.

Criar uma lista de 3 frutas e outra de 3 vegetais

'''

frutas = ['maçã','banana','uva']
vegetais = ['cenoura','alface','cebola']

for i in frutas:
    print()
    for j in vegetais:
        print(i,"e", j)
