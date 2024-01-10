from datetime import datetime

print('----- Aula 78 -----')
# A78 - Conhecendo Classes

print('Teoria - checar as anotações')

print('----- Aula 79 -----')
# A79 - Criando a sua Primeira Classe

class Funcionarios:
    nome = 'Jorge'
    sobrenome = 'Mateus'
    data_nascimento = '10/12/1977'

usuario1 = Funcionarios()

usuario1.nome
usuario1.sobrenome
print(usuario1.nome + " " + usuario1.sobrenome + " - " + usuario1.data_nascimento)

print('----- Aula 80 -----')
# A80 - Criando Objetos dentro de uma Classe

# Criando a Classe
class Funcionarios2:
    pass

# Criando o Objeto
usuario2 = Funcionarios2()
usuario3 = Funcionarios2()

# Criando os parâmetros do usuario2
usuario2.nome = 'Vicente'
usuario2.sobrenome = 'Marcelo'
usuario2.data_nascimento = '04/01/1991'

# Criando os parâmetros do usuario3
usuario3.nome = 'Levi'
usuario3.sobrenome = 'Benjamin'
usuario3.data_nascimento = '10/01/1957'

# Print
print(usuario2.nome + " " + usuario2.sobrenome + " - " + usuario2.data_nascimento)
print(usuario3.nome + " " + usuario3.sobrenome + " - " + usuario3.data_nascimento)


print('----- Aula 81 -----')
# A81 - Criando Construtores
# Construtores reduzem a passagem de parâmetros

class Funcionarios3:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome # self é como se fosse o this em Java.
        self.sobrenome = sobrenome # this.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

usuario4 = Funcionarios3('Eduarda','Isabela','06/01/1980')
usuario5 = Funcionarios3('Malu','Alana','07/01/2002')

print(usuario4.nome + " " + usuario4.sobrenome + " - " + usuario4.data_nascimento)
print(usuario5.nome + " " + usuario5.sobrenome + " - " + usuario5.data_nascimento)

print('----- Aula 82 -----')
# A82 - Adicionando mais funções a Classe
# Fazer uma função para imprimir os dados dos funcionários.

class Funcionarios4:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

    def nome_completo(self):
        return self.nome + " " + self.sobrenome

usuario6 = Funcionarios4('Marcos','Santos','06/01/1967')

print(usuario6.nome + " " + usuario6.sobrenome + " - print dos parâmetros")
print(usuario6.nome_completo()  + " - função")
print(Funcionarios4.nome_completo(usuario6) + " - chamando a classe e a função")
# dentro da classe "Funcionarios4", tenho a função "nome_completo" que tem o objeto "usuario6"

print('----- Aula 83 -----')
# A83 - Calculando a idade do funcionário
# Fazer uma função que calcula a idade dos funcionários

class Funcionarios5:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento
        # return int (2024 - self.ano_nascimento) --> o 2024 é impraticavel, pois iria ter que mudar todo ano
        # para o Python buscar no sistema o ano, é necessário importar
            # from datetime import datetime - linha 1

usuario7 = Funcionarios5("Danilo","Tomás",2001)
print(Funcionarios5.idade_funcionario(usuario7))


