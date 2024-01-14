# A159 - Desafio 32 - Lambda com For
'''

Crie uma função lambda que eleve um número ao quadrado. Em seguida, use essa função para
calcular o quadrado de todos os números em uma lista usando um "for".

'''

quadrado = lambda x: x**2

numeros = list(range(1, 7))
resultados = []

for i in numeros:
    resultados.append(quadrado(i))

print(resultados)
