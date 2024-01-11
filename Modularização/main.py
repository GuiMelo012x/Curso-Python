from funcoes import find_index
# from funcoes import somar
# from funcoes import multi --> outra maneira de importar, mas apenas a funcao em si.
from Itens.cadastro import cliente # Aula 86

# A84 - Criando seu primeiro Modulo
    # Funções criadas no módulo "funcoes.py"

# A85 - Importando um Modulo
    # é necessário chamar lá em cima, e pode usar import e from.
        # o import importa tudo, o from puxa apenas algumas funções.

# A86 - Criando e Importando Packages
    # foi criado a pasta itens com cadastro.py e calculo.py
        # from itens.cadastro import cliente (linha 4)

print('----- Aula 87 -----')
# A87 - Aplicando um módulo
# Fazer uma lista, depois, criar uma função que procure se eu passar um item
# que está dentro desta lista, dizer em que index o item está, caso contrário,
# passa um numero negativo.
    # A lista estará no arquivo principal, e a funcao estará dentro do módulo funcoes.py .

list1 = ['a','b','c','d','e']

var1 = find_index(list1,'c')
print(var1)

