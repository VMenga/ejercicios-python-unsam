#costo_camion.py
#Por Valentin Mengascini
import os
import csv

costo = 0
f = csv.reader(open('camion.csv', 'rt'), delimiter=',')
header = next(f)
for row in f:
    costo_cajones = int(row[1]) * float(row[2])
    costo = costo + costo_cajones

print('Costo total:', costo)
