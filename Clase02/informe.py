#informe.py
#Por Valentin Mengascini
import csv
import sys

def leer_camion(archivo_camion):
    camion = []
    dicc = {}
    f = csv.reader(open(archivo_camion, 'rt'), delimiter=',')
    header = next(f)
    for row in f:
        dicc['nombre'] = str(row[0])
        dicc['cajones'] = int(row[1])
        dicc['precio'] = float(row[2])
        camion.append(dicc)
    return camion

'''
def leer_precios(archivo_precios):
    precios = csv.reader(open(archivo_precios, 'rt'), delimiter=',')
    venta_fruta = 0
    for linea in precios:
        venta_fruta = linea[1]
    pass

'''
camion = leer_camion('camion.csv')
total = 0
for s in camion:
    total += s['cajones']*s['precio']

print(total)
