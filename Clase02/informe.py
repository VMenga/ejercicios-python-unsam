#informe.py
#Por Valentin Mengascini
import csv
import sys

def leer_camion(archivo_camion):
    costo = 0
    f = csv.reader(open(archivo_camion, 'rt'), delimiter=',')
    header = next(f)
    for row in f: 
        costo += int(row[1]) * float(row[2])
    return costo


def leer_precios(archivo_precios):
    precios = csv.reader(open(archivo_precios, 'rt'), delimiter=',')
    precio_fruta = 0
    for linea in precios:
        if fruta in linea:
            precio_fruta = linea[1]
