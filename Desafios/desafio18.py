# A131 - Desafio 18 - Procura em Listas
'''

Imagine que você tem uma loja de carros, e crie uma lista com os carros que você tem em estoque.
Os carros são "Sandero","Gol","HB20". Peça ao usuário para que ele insira o nome do carro que deseja comprar.
Se o carro estiver em estoque, imprima "Este carro está disponível". Se o carro não estiver em estoque,
imprima "Desculpe, este carro não está disponível."

Bônus: trabalhar com lower case

'''

carros = ['sandero','hb20','gol']

pedido = input('Digite o carro que você procura: ')

if pedido.lower() in carros:
    print('Este carro está dispon ível')
else:
    print('Este carro não está disponível')
