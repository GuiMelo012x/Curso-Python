# A36 - While Loops - Programa em que um produto cai 5 reais por dia, até 20. Se acabar o estoque antes, encerra o programa.
print('----- Aula 36 -----')
valor = 100
dia = 0
while valor > 20:
    print(f' dia {dia+1} = R$ {valor},00')
    dia += 1
    valor -=5

print('----- Aula 37 -----')

# A37 - Operador Ternário - Programa que checa se a pessoa pode ou não votar nas eleições.
idade = 14

if (idade >= 16):
    resultado = print('Pode votar')
else:
    resultado = print('Não pode votar - Else')

resultado = 'Pode votar' if idade >= 16 else 'Não pode votar'
print(resultado + ' - Operador Ternário')
# Todo o if e else das 4 linhas anteriores foram reduzidas em apenas uma linha.


# A38 - Diferença entre While, For e If-Else

print('----- Aula 39 -----')

# A39 - Break - Fazer um programa que calcula a comissão de um produto acima de R$ 20 publicado no site
valor = int (input ('Insira o valor do seu produto:'))

print(valor)

while valor > 20:
    valor = (valor * 0.10) + valor
    print(f'O valor final do seu produto será de R$ {valor}')
    break