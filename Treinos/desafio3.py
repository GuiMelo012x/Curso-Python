# A93 - Sets (Desafio) - Filtrando funcionários em uma empresa
'''

Criar um programa que gera 3 listas de acordo com a necessidade logo abaixo:

Lista1 = Funcionários que tem carro e trabalham de noite
Lista2 = Funcionários que tem carro e trabalham de dia
Lista3 = Funcionários que não tem carro

'''

funcionarios = ['Ana', 'Marcos','Alice','Pedro','Sophia','Bruno','Melissa']
turno_dia = ['Ana','Marcos','Alice','Melissa']
turno_noite = ['Pedro','Sophia','Bruno']
tem_carro = ['Marcos','Alice','Bruno','Melissa']


print('----- Minha Solução -----')

# Tem carro e trabalha de noite -->  apenas bruno
lista1 = set(tem_carro) & set (turno_noite)
print(f' Lista 1 = {list(lista1)}')

# Tem carro e trabalha de dia --> marcos, alice e melissa
lista2 = set(tem_carro) & set(turno_dia)
print(f' Lista 2 = {list(lista2)}')

# Não tem carro -->Ana, Pedro e Sophia
lista3 = set (tem_carro) ^ set (funcionarios)
print(f' Lista 3 = {list(lista3)}')

print()

print('----- Solução do Professor -----')

lista1 = set(tem_carro).intersection(turno_noite)
print(lista1)

lista2 = set(tem_carro).intersection(turno_dia)
print(lista2)

lista3 = set(funcionarios).difference(tem_carro)
print(lista3)
