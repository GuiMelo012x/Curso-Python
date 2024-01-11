# A84 - Criando seu primeiro Modulo
def somar():
    print('Esta funcao vai somar valores')

def mult():
    print('Esta funcao vai multiplicar valores')

# A87 - Aplicando um módulo
def find_index(to_find, item): # to_find = o item que quero procurar | item = o item que vai ter ou não.
    for i, valor in enumerate(to_find):
        if valor == item:
            return i

    return -1