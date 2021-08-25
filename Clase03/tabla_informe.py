#informe.py
#Por Valentin Mengascini
import csv
import sys

def hacer_informe(camion, precios):
    

#Esta funcion crea una lista de diccionarios con el stock
def leer_camion(archivo_camion):
    camion = []
    f = csv.reader(open(archivo_camion, 'rt'), delimiter=',')
    encabezados = next(f)
    for n_fila, fila in enumerate(f, start=1):
        record = dict(zip(encabezados, fila))
        try:
            dicc = {}
            dicc['nombre'] = str(record['nombre'])  #Lo que hice fue modificar esto para que
            dicc['cajones'] = int(record['cajones']) #arme la lista de diccionarios igual que antes
            dicc['precio'] = float(record['precio']) #Pero sin depender de la posicion de la fila[]
            camion.append(dicc)
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
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

#Programa:
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


'''
Salida de prueba:
    python3 informe.py ../Data/fecha_camion.csv ../Data/precios.csv
        Costo total del camion: $47671.15
        Total de facturacion: $62986.1
        La ganancia total fue de : $15314.95

    python3 informe.py ../Data/camion.csv ../Data/precios.csv
        Costo total del camion: $47671.15
        Total de facturacion: $62986.1
        La ganancia total fue de : $15314.95

█████████████████████████████████████
█████████████████████████████████████
████ ▄▄▄▄▄ █▀▀ ██▀▀ ▀  ▄▀█ ▄▄▄▄▄ ████
████ █   █ █▄▀██▀█▄▀▀▄█▄▄█ █   █ ████
████ █▄▄▄█ █ ▄ █ ▀▀ ▀  ▀██ █▄▄▄█ ████
████▄▄▄▄▄▄▄█ █ ▀▄█ █▄▀ ▀▄█▄▄▄▄▄▄▄████
████  ▀▄▀█▄▄█▀█  ▀ █▀▀▀█▀█ ▄▄▀▄▄▀████
█████▀ ▄▄▄▄  ▀▀  ▀█▀▄▄▀▄▄█▄▀▀▄  █████
████▀ ▀█▄ ▄█▄▀▄ █▄█▀█ █ ▄ ▄▀█▄█▄▄████
█████▄▄▀ ▀▄ ▀▄▄ █  ▀   ▀ ▄▀██ ▄ ▄████
█████ ▄ ▄▄▄ ██ █ ▄██▀▄▀▄▄▄▀ █▀█▄▀████
████▄█▄█▄▀▄█▀▀▀▄ █▄▀█▀█▀▄▄ ▄███  ████
████▄██▄█▄▄█   ▀█ ▄▄█▀█▀ ▄▄▄ █ ▀▀████
████ ▄▄▄▄▄ █▄▄ ██▀▄█▀▄ █ █▄█ ▀▀▄▀████
████ █   █ █▀ ▀▀ █▀██▄█▀▄▄ ▄ ▀▀▀█████
████ █▄▄▄█ █▀█▄█ ▀▀█▀ ▄▄▀▄██ ▄▄▀▄████
████▄▄▄▄▄▄▄█▄██▄▄▄▄▄▄▄▄█▄██▄▄██▄█████
█████████████████████████████████████
█████████████████████████████████████
'''
