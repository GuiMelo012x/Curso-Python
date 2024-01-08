from array import array

print('------ Aula 58 -----')
# A58 - Arrays
# Utiliza-se Arrays quando uma lista é muito grande.
# deve-se importar com a linha de código "from array import array" (linha 1)

letras = ['a','b','c','d']
numeros_i = [10,20,30,40]
numeros_f = [1.2,2.2,3.2]

print(letras)
print(numeros_i)
print(numeros_f)
print()

letras = array('u', ['a','b','c','d']) # u = string
inteiros = array('i', [10, 20, 30, 40]) # i = integer
float = array('f', [1.2, 2.2, 3.2]) # f = float

print(letras)
print(inteiros)
print(float)

print('----- Aula 59 -----')

# A59 - Criando Sets
# Set é similar a listas, evita itens duplicados e não utiliza index

list1 = [10,20,30,40,50]
list2 = [10,20,60,70]

num1 = set(list1)
num2 = set(list2)

print(num1 | num2) # | = Union. Ele unifica as 2 listas e não repete os valores que estão repetidos, mas ainda os mostra.
print(num1 - num2) # - = Difference. Ele mostra apenas os números que estão na lista 1 e não na lista 2.
print(num1 ^ num2) # ^ = Symmetric Difference. Ele mostra as 2 listas juntas, e retira os valores repetidos, mostrando apenas os que não se repetem.
print(num1 & num2) # & = And. Mostra apenas os itens que estão duplicados nas 2 listas.

print(len(num1))
# print(num1[0]) -> não funciona

print('----- Aula 60 -----')

# A60 - Funções em Sets

list1 = set([1,2,3,4,5,6])

s1 = {1,2,3,4,5,6,1,2,3}

s1.add(7)
s1.add(1)
s1.update([1,2,8,9]) # ignora o 1 e o 2 pois já existia.
s1.remove(9)
s1.discard(8)
# remove e discard fazem a mesma coisa, só que o remove dá erro se o item não estiver no set.

print(s1)

print('----- Aula 61 -----')

# A61 - Sets com Strings

set1 = {'a','b','c'}
set2 = {'a','d','e'}
set3 = {'c','d','f'}

set4 = set1.union(set2)
print(f'{set4} - Union') # une os 2.

set4 = set1.difference(set3)
print(f'{set4} - Difference') # mostra oq tem apenas no set1.

set4 = set1.intersection(set2)
print(f'{set4} - Intersection') # mostra oq tem em comum nos 2.

set4 = set1.symmetric_difference(set3)
print(f'{set4} - Symmetric Difference') # mostra oq tem em comum nos 2 e remove os duplicados.



