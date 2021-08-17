#costo_camion.py
#Por Valentin Mengascini
import sys
import csv

def costo_camion(nombre_archivo):
    costo = 0
    f = csv.reader(open(nombre_archivo, 'rt'), delimiter=',')
    header = next(f)
    for row in f:
        costo_cajones = int(row[1]) * float(row[2])
        costo = costo + costo_cajones
    return costo
#    print("Costo total del camion: $", total, sep='')

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)

'''
Ejemplos de salida:
python3 camion_commandline.py
Costo total: 47671.15

python3 camion_commandline.py ../Data/camion2.csv
Costo total: 19908.75
'''
