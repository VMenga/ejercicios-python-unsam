#invlista.py
#Por Valentin Mengascini

def invertir_lista(lista):
    invertida = []
    for elemento in lista:
        invertida.insert(0, elemento)
    return invertida
