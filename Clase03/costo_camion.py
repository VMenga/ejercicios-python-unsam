#costo_camion.py
#Por Valentin Mengascini
import os
import csv

def costo_camion(nombre_archivo):
    f = csv.reader(open(nombre_archivo, 'rt'), delimiter=',')
    encabezados = next(f)
    costo_total = 0
    for n_fila, fila in enumerate(f, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        # Esto atrapa errores en los int() y float() de arriba.
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return costo_total

archivo = input("Ruta del archivo:")
print(costo_camion(archivo))
'''
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
