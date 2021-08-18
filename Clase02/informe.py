#informe.py
#Por Valentin Mengascini

#Solo anda la funcionalidad de crear el diccionario
#del costo de camion, la de crear el dicc de leer_precios
#Solo devuelve el ultimo valor repetidas veces y no encontre el problema

import csv
import sys

def leer_camion(archivo_camion):
    camion = []
    f = csv.reader(open(archivo_camion, 'rt'), delimiter=',')
    header = next(f)
    for row in f:
        dicc = {}
        dicc['nombre'] = str(row[0])
        dicc['cajones'] = int(row[1])
        dicc['precio'] = float(row[2])
        camion.append(dicc)
    return camion

def leer_precios(archivo_precios):
    p = csv.reader(open(archivo_precios, 'rt'), delimiter=',')
    precio = []

    for row in p:
        if len(row) != 0:
            dicc2 = {}
            dicc2['nombre'] = str(row[0])
            dicc2['precio'] = float(row[1])
            precio.append(dicc2)
        else:
            continue
    return precio


if len(sys.argv) == 3:
    nombre_archivo = sys.argv[1]
    archivo_precios = sys.argv[2]
else:
    nombre_archivo = input("Ingrese ruta del archivo camion.csv: ")
    archivo_precios = input("Ingrese ruta del archivo precios.csv: ")

camion = leer_camion(nombre_archivo)
total_camion = 0
total_entrada = 0
neto = 0

for s in camion:
    total_camion += s['cajones']*s['precio']


print("Costo total del camion: $", total_camion, sep = '')
