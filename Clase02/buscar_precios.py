#buscar_precios.py
#Por Valentin Mengascini
import os
import csv

def buscar_precio(fruta):
    precios = csv.reader(open('precios.csv', 'rt'), delimiter=',')
    precio_fruta = None

    for linea in precios:
        if fruta in linea:
            precio_fruta = linea[1]

    if precio_fruta == None:
        print("No tenemos", fruta, "en nuestra lista de precios.")
    else:
        print("El precio de ", fruta," es de: $", precio_fruta,"/kg", sep='')

'''
Dejo una prueba de la salida de la funcion:

>>> buscar_precio("Naranja")
El precio de Naranja es de: $106.28/kg
>>> buscar_precio("Kiwi")
No tenemos Kiwi en nuestra lista de precios.

Nota: el archivo 'precios.csv' en este caso esta en la misma
carpeta que el archivo buscar_precios.py
'''
