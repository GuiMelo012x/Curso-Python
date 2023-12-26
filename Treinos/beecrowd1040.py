n1 = float(input('Digite a primeira nota: ')) 
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1)) / 10
print(f'Media: {media}')


if media >= 7:
    print(f'A média do aluno foi {media}. Aluno aprovado.')
elif media < 7 and media > 5:
    print('Aluno em exame.')
else:
    print(f'A média do aluno foi: {media}. Aluno reprovado.')
    
notaExame = float(input('Digite a nota do exame: '))

print(f'Nota do exame: {notaExame}')

novaMedia = (notaExame + media)
if novaMedia >= 5:
    print('Aluno aprovado.')
    
print(f'Media final: {novaMedia/2}')
