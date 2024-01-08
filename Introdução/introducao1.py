# Comentários - com #

x = 2
print(x+80) # já printa 82

x = str("3") # agora é considerado como string
y = int(4) # agora é considerado int
z = float(5) # agora é considerado float
w = str("oii") #string

print(x)
print(y)
print(z)

nome = "André"
idade = 32 # 32 é int.
idade = str(idade) # 32 e todo o conteudo de idade é string.
cidade = "São Paulo"
print('O ' + nome + " tem " + idade + " anos de idade e mora na cidade de " + cidade + '.')

# o André tem 32 anos de idade e mora na cidade de São Paulo.


# INPUT

'''
nome2 = input('Digite o seu nome: ')
idade2 =input('Digite a sua idade: ')
cidade2 = input('Digite sua cidade: ')


print('O ' + nome2 + " tem " + idade2 + " anos de idade e mora na cidade de " + cidade2 + '.')


# Programa que calcula idade

ano_nascimento = input("Digite o seu ano de nascimento: ")
idade3 = 2023 - int(ano_nascimento)

print(idade3)
'''

# SLICING

fruta = 'Abacate'
print(fruta[3]) # 0 - A / 1 - B / 2- A / 3 - C / 4 - A / 5 - T / 6 - E /

valor = 99.75
valor = str(valor)

print(valor[2:]) # pega o .75 pois conta 2 espaços.


# IMPRIMIR O Marcos Silva é um excelente [Programador]

nome = 'Marcos'
sobrenome = 'Silva'
profissao = 'Programador'

texto = 'O ' + nome + " " + sobrenome + " é um excelente " + '[' + profissao + ']'

print(texto)

texto2 = f'0 {nome} {sobrenome} é um excelente [{profissao}]'

print(texto2)
# MÉTODOS DE STRING

mensagem = 'Eu adoro programacao'

print(mensagem.upper())
print(mensagem.lower())
print(mensagem.replace('adoro','amo')) # troca o "adoro" por "amo".
print(mensagem.capitalize()) # deixa em maiúsculo a primeira letra.
print(mensagem.find('a')) # procura em que local está a letra ou em que ponto começa uma palavra.
print(mensagem.find('adoro'))
print(mensagem.strip()) # remove qualquer espaço que tenha antes do primeiro caracter.
