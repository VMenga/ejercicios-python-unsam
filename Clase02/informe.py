#informe.py
#Por Valentin Mengascini
import csv
import sys

#Esta funcion crea una lista de diccionarios con el stock
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

#Esta funcion crea un diccionario con los precios por nombre de fruta
def leer_precios(archivo_precios):
    p = csv.reader(open(archivo_precios, 'rt'), delimiter=',')
    precios = {}
    for row in p:
        if len(row) != 0:
            precios[str(row[0])] = float(row[1])
        else:
            continue
    return precios

#Esta condicion chequea si los archivos csv estan incluidos como argumento en el comando
if len(sys.argv) == 3:
    nombre_archivo = sys.argv[1]
    archivo_precios = sys.argv[2]
else:
    nombre_archivo = input("Ingrese ruta del archivo camion.csv: ")
    archivo_precios = input("Ingrese ruta del archivo precios.csv: ")


camion = leer_camion(nombre_archivo)
precios = leer_precios(archivo_precios)
total_camion = 0
total_entrada = 0
neto = 0

#Costo del camion
for s in camion:
    total_camion += s['cajones']*s['precio']
print("Costo total del camion: $", total_camion, sep = '')

#Total de ventas
for s in camion:
    total_entrada += s['cajones']*precios[s['nombre']]
print("Total de facturacion: $", total_entrada, sep='')

#Ganancia o perdida
neto = total_entrada - total_camion
if neto >= 0:
    print("La ganancia total fue de : $", round(neto, 2), sep='')
else:
    print("Hubo una perdida de : $", round(-neto, 2), sep='')
