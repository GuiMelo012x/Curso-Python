import math

print('----- Aula 40 -----')
# A40 - Funções - Início
    # Dry - Don't Repeat Yourself.

def boas_vindas():
    print('Olá')
    print('Bom Dia')

boas_vindas() # printa Olá, bom dia

print('----- Aula 41 -----')
# A41 - Variáveis dentro da Função
def soma():
    n1 = 10
    n2 = 20
    resultado = n1 + n2
    print(resultado)


soma()

print('----- Aula 42 -----')

# A42 - Funções com parâmetros e argumentos

def boas_vindas(nome,quantidade):
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} cadernos em estoque')

boas_vindas('Joao',5)
boas_vindas('Marcos',4)
boas_vindas('Sergios',3)

'''
3 funções em apenas 3 linhas.

def boas_vindas_Joao():
    print('Olá Joao')
    print('Temos 5 cadernos em estoque')

def boas_vindas_Marcos():
    print('Olá Marcos')
    print('Temos 4 cadernos em estoque')

def boas_vindas_Sergio():
    print('Olá Sergio')
    print('Temos 3 cadernos em estoque')
'''

print('----- Aula 43 -----')
# A43 - Argumentos Default e Non - Default
    # Default - Aquele que você define o valor no parâmetro
    # Non - Default - Aquele que você não define o valor no parâmetro

def bem_vindo(nome,quantidade=6): # nome = non-default | quantidade = default. O default deve estar sempre em último
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} cadernos em estoque')

def bem_vinda(quantidade,nome='Lia'): # nome = default | quantidade = non-default . O default deve estar sempre em último
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} cadernos em estoque')

bem_vindo('Chico') # Printa o Chico que eu passei, e que tem 6 cadernos, pois é o default da função.
print()
bem_vinda(5) # Printa o 5 que eu passei, e o nome 'Lia', pois é o default da função.

print('----- Aula 44 -----')

# A44 - Print e Return em Funções

def cliente1(nome):
    print(f'Olá {nome}')

cliente1('Maria')

def cliente2(nome):
    return f'Olá {nome}'

print(cliente2('Cristian'))

print('----- Aula 45 -----')

# A45 - Argumentos - XArgs - Criar uma função que soma vários números

def somar(*numeros): # Quando põe o asterisco, significa que vários números podem entrar na função, e não há um definido. (def soma já existe na Aula 41).
    resultado = 0 # ponto de início
    for num in numeros:
        resultado += num
    return resultado

x = somar(2,3,4,7)
print(x)

print('----- Aula 46 -----')

# A46 - Vários argumentos xargs nomeando argumentos - Criar uma função que armazena números e strings

def agencia(**carro): # dois asteriscos significam que você pode passar os parâmetros embaixo
    return carro

print(agencia(marca = 'Gol', cor = 'Branco', motor = 1.0, placa = 1234))
print(agencia(marca = 'Gol', cor = 'Preto', motor = 1.0))
print(agencia(marca = 'Gol', cor = 'Azul'))

print('----- Aula 47 -----')

# A47 - Importando um Módulo
# Qual o fatorial de quatro? R = 4 * 3 * 2 *1 = 24

fatorial = 4*3*2*1
print(f'Calculado manualmente - {fatorial}')

# Agora, qual o fatorial de 10? Como é longo, podemos usar a biblioteca "Math"
# Deve-se importar o módulo math (checar na linha 1)

print(f'Calculado com a biblioteca math - {math.factorial(4)}')
print(f'Fatorial de 10 com a biblioteca math - {math.factorial(10)}')

print(math.floor(2.7)) # arredonda pra baixo.
print(math.ceil(2.7)) # arredonda pra cima.











