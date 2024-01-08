print('----- Aula 62 -----')

# A62 - Introdução a Dicionários
    # Dicionários utilizam index no formato de keys e de values, e aceita string, int, float, boolean.

aluno = {'nome':'Ana', 'idade': 16, 'nota final': 'A','aprovação': True}
        # nome = key | Ana = value .... idade = key | 16 = value etc.

print(aluno['nome']) # pois usa o index no formato de keys e values

print('----- Aula 63 -----')

# A63 - Atualizando o Dicionário

aluno = {'nome':'Ana', 'idade': 16, 'nota final': 'A','aprovação': True}

aluno['nome'] = 'José'
print(aluno['nome'])

aluno.update({'nome': 'José', 'nota final': 'B'}) #atualiza mais de um ao mesmo tempo
print(aluno)

aluno.update({'nome': 'José', 'nota final': 'B', 'endereco': 'Rua A'}) # além de atualizar, também adiciona.
print(aluno)

print(aluno.get('nome', 'não existe') + ' - método get')

del aluno['idade']
print(aluno)

print('----- Aluno 65 -----')
# A65 - Looping dentro de um dicionário

for i in aluno:
    print(aluno[i])

print()

for i in aluno.values():
    print(i)

print()

for keys,values in aluno.items():
    print(keys, values)


print('----- Aula 66 -----')

# A66 - Visualizando Itens, Keys e Values

aluno = {'nome':'Ana',
         'idade': 16,
         'nota final': 'A',
         'aprovação': True,
         'materias': ['Fisica', 'Matematica', 'Inglês']
         }

print(aluno.get('materias')) # mostra as 3 materias q ela faz
print(len(aluno)) # mostra a quantidade de keys (5)
print(aluno.keys()) # mostra as keys
print(aluno.values()) # mostra os values
print(aluno.items()) # mostra os itens (keys e values)

