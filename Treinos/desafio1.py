# A89 - If Else (Desafio) - Ponto do Steak
'''
Criar um programa que dependendo da temperatura(em celsius) da carne ele retorna o ponto de cozimento.
O usuário deverá fornecer a temperatura

Temperaturas - Cozimento
Abaixo de 48° C - Cozinhar mais
48°C - Selada
54°C - Ao ponto para mal-passada
60°C - Ao ponto
65°C - Ao ponto para bem-passada
71°C - Bem passada
Acima de 80°C - Queimou

'''

temperatura_usuario = int(input('Digite a temperatura em Celsius: '))


print('----- Minha Solução -----')
if temperatura_usuario >= 48 and temperatura_usuario < 54:
    print('Selada')
elif temperatura_usuario >= 54 and temperatura_usuario < 60:
    print('Ao ponto para mal-passada')

elif temperatura_usuario >= 60 and temperatura_usuario < 65:
    print('Ao ponto para bem-passada')

elif temperatura_usuario >= 65 and temperatura_usuario <= 79:
    print('Bem-passada')

elif temperatura_usuario >= 80:
    print('Queimou')
else:
    print('Cozinhar mais')


print('----- Método do Professor -----')
''' 
Método do professor:  utilizar o in range
'''

if temperatura_usuario < 48:
    print('Cozinhar mais')
elif temperatura_usuario in range(48,53):
    print('Selada')
elif temperatura_usuario in range (54,59):
    print('Ao ponto para mal passada')
elif temperatura_usuario in range (60,64):
    print('Ao ponto')
elif temperatura_usuario in range (65,70):
    print('Ao ponto para bem passada')
elif temperatura_usuario in range (71,80):
    print('Bem passada')
elif temperatura_usuario >= 80:
    print('Queimou')
