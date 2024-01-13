# A101 - Desafio 03 - Números.
'''

Declare duas variáveis: num1, que deve guardar um número inteiro "10", e num2, que deve guardar um
float "3.5". Depois disso, realize a divisão de num1 por num2 e imprima

'''

def calcular(num1,num2):
    resultado = num1/num2
    print(type(num1))
    print(type(num2))
    return resultado

print('O resultado da divisão é',calcular(10,3,5))
