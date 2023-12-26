velocidade = 40
if velocidade > 110:
    print('Acima da velocidade permitida.')
    print('Favor reduzir a sua velocidade.')

elif velocidade < 60:     # pode ter quantos quiser
    print('Dirija acima de 80km/h')

else:
    print('Velocidade ok')


renda_acima_5mil = False
nome_limpo = True

if renda_acima_5mil and nome_limpo:
    print('Financiamento aprovado')
else:
    print('Financiamento negado')
    
    
valor = 20

# if valor >= 20 and valor < 40: - no entanto, tem como escrever isto de forma mais fácil:

if 20 <= valor < 40:
    print("Valor aceito") 
    
else:
    print("Valor não aceito")