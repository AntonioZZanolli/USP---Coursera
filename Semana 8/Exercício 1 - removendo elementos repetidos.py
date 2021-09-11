lista = []

def remove_repetidos(lista):
    sorted(lista)
    lista2 = []
    for x in lista:
        if x not in lista2:
            lista2.append(x)
    lista2.sort()
    return lista2
    
