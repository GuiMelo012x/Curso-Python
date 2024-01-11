# A91 - Funções (Desafio) - Calculadora para Pintura

'''

Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede. O usuário
deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem: "Você necessita de x latas de tinta".

'''



rendimento = int(input('Qual é o rendimento da lata? '))
altura = int(input('Qual é a altura da parede? '))
largura = int(input('Qual é a largura da parede? '))
print()

print('----- Minha Solução -----')
def calcular():
    parede = altura * largura
    qtd_latas = parede / rendimento
    return qtd_latas

print(f'Você precisa de {calcular()} latas de tinta.')


print()

print('----- Solução do Professor -----')

def calculo_tinta():
    area = altura * largura
    total = area/rendimento
    print(f'Você precisa de {total} latas de tinta')

calculo_tinta()
