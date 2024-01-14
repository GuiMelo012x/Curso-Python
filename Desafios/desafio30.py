# A155 - Desafio 30 - Multiplicando com Lambda
'''

Crie uma função lambda que aceite dois números e retonre a multiplicação desses números.

'''

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

mult = lambda x,y: x*y
print(mult(2,5))
print(mult(x,y))

print('---- Com Função: -----')

def multiplicar(a,b):
    return a*b

print(multiplicar(5,10))
