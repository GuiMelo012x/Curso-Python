print('----- Aula 74 -----')

# A74 - O que são erros
print('Teoria')

print('----- Aula 75 -----')

# A75 - Try e Exception em uma Lista

try:
    letras = ['a','b','c']
    print(letras[3]) #erro
except IndexError:
    print('Index não existe.') # se der indexerror, ele não dará erro, ele vai dar uma exceção.



print('----- Aula 76 -----')

# A76 - Try e Exception com o input.
# Fazer um programa em que o usuário digita em número inteiro o valor do produto que quer vender.


valor = int(input('Digite o valor do seu produto: ')) # quando eu digito uma letra, dá "ValueError" e encerra o programa
# Consertando:
try:
    valor = int(input('Digite o valor do seu produto: '))
except ValueError:
    print('Digite um valor válido.') # vai dar erro, porém o programa não vai encerrar.

print('Programa continuou depois do erro.')


print('----- Aula 77 -----')

# A77 - Adicionando o Else e Finally
# Fazer um programa em que o usuário digita em número inteiro o valor do produto que quer vender.
# Porém, se der certo, ele continua o programa e calcula a comissão do produto e diz o valor final.

try:
    valor = int(input('Digite o valor do seu produto: '))
except ValueError:
    print('Digite um valor válido.') # vai dar erro, porém o programa não vai encerrar.
else:
    print('Usuário digitou um valor correto.')
    comissão = valor * 0.3
    print(f' o valor do produto será de R$ {valor + comissão}.')

# Se eu digitar correto, o else será ativado e o exception não.
# Se eu digitar errado, o exception será ativado e o else não.

try:
    valor = int(input('Digite o valor do seu produto: '))
except ValueError:
    print('Digite um valor válido.') # vai dar erro, porém o programa não vai encerrar.
finally:
    print('Código finalizado.')
