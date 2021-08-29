#busqueda_en_listas.py
#Por Valentin Mengascini

def buscar_u_elemento(lista, elemento):
    posicion = -1
    for indice, z in enumerate(lista):
        if z == elemento:
            posicion = indice
            break
    return posicion

def maximo(lista):
    maximo = lista[0]
    for elemento in lista:
        if elemento > maximo:
            maximo = elemento
    return maximo
