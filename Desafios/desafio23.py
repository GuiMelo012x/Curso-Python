# A141 - Desafio 23 - Comparação de Sets
'''

Crie dois conjuntos, cada um contendo 5 nomes. Alguns nomes devem estar presentes em ambos os conjuntos.
Use um método para encontrar quais nomes aparecem em ambos os conjuntos e imprima o resultado.

'''

s1 = {'Chandler', 'Monica', 'Joey', 'Ross', 'Rachel'}
s2 = {'Chandler', 'Monica', 'Joey', 'Phoebe', 'Mike'}

print(s1.union(s2), ' - Todos os nomes que aparecem nas listas, sem repetir.')


print(s1.symmetric_difference(s2), ' - São exclusivos de apenas uma lista.')

print(s1.difference(s2),' - São exclusivos da lista 1.')
print(s2.difference(s1),' - São exclusivos da lista 2.')

print(s1.intersection(s2),' - Aparecem nas 2 listas.') # Resposta.
