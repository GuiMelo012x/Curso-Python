# A105 - Desafio 5 - Cálculos Matemáticos.
'''

Crie um script que solicite ao usuário dois números. Em seguida ,seu script deve imprimir a soma,
subtração, multiplicação, divisão, e a exponenciação desses dois números.

'''
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
print()
def soma(num1,num2):
    return print('Soma:',num1 + num2)

def subtracao (num1,num2):
    return print('Subtração:', num1-num2)


def multiplicacao(num1,num2):
    return print('Multiplicação:', num1*num2)

def divisao(num1,num2):
    return print('Divisão:', num1/num2)

def exponenciacao(num1,num2): # ** = elevado
    return print('Exponenciação:',num1**num2)


soma(num1,num2)
subtracao(num1,num2)
multiplicacao(num1,num2)
divisao(num1,num2)
exponenciacao(num1,num2)


