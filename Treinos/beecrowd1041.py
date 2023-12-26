x = float(input('Digite a Coordenada X: '))
y = float(input('Digite a Coordenada Y: '))

if x > 0 and y > 0:
    print('Q1')

elif x > 0 and y < 0:
    print('Q4')

elif x < 0 and y > 0:
    print('Q2')

elif x < 0 and y < 0:
    print('Q3')

elif x == 0:
    print(f'Está sob o eixo X no ponto {y} Y')

elif y == 0:
    print(f'Está sob o eixo Y no ponto {x} X')

else:
    print('Origem')
