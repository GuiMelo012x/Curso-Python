# Aula 153 - Desafio 29 - Convertendo para Lambda
'''

Crie uma função lambda que aceite um número e retorne o cubo deste número.

Bônus: soma.

'''
x = int(input('Digite um número: '))

print('----- Cubo: -----')
cubo = lambda x: x**3
print(cubo(x))



print('----- Soma: -----')
x = 1
y = 2
soma = lambda x,y: x + y
print(soma(x,y))
print(soma(5,3))

print('\n----- Resolvendo Sem Lambda: -----')

def cubo(num):
    return num**3
# cubo = lambda: x**3
def soma(num1,num2):
    return num1+num2

print(cubo(3))
print(soma(10,3))
