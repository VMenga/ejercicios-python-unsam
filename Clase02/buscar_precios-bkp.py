#buscar_precios.py
#Por Valentin Mengascini
import os
import csv

fruta = input("Ingrese fruta a buscar: ")
precios = csv.reader(open('precios.csv', 'rt'), delimiter=',')
precio_fruta = None

for linea in precios:
    if fruta in linea:
        precio_fruta = linea[1]

if precio_fruta == None:
    print("No tenemos", fruta, "en nuestra lista de precios.")
else:
    print("El precio de ", fruta," es de: $", precio_fruta,"/kg", sep='')
