#informe.py
#Por Valentin Mengascini
import csv
import sys

def leer_camion(archivo_camion):
    costo_camion = 0
    f = csv.reader(open(archivo_camion, 'rt'), delimiter=',')
    header = next(f)
    for row in f:
        costo_camion += int(row[1]) * float(row[2])
    return costo_camion


def leer_precios(archivo_precios):
    precios = csv.reader(open(archivo_precios, 'rt'), delimiter=',')
    venta_fruta = 0
    for linea in precios:
        venta_fruta = linea[1]
    pass


for s in costo_camion:
    total += s['cajones']*s['precio']
