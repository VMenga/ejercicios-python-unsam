#arboles.py
#Por Valentin Mengascini
import csv
import sys
from pprint import pprint

def leer_parque(nombre_archivo, parque):
    lista_arboles = []
    f = csv.reader(open(nombre_archivo, 'rt'), delimiter=',')
    encabezados = next(f)
    for n_fila, fila in enumerate(f, start=1):
        record = dict(zip(encabezados, fila))
        if record['espacio_ve'] == parque:
            try:
                dicc = {}
                dicc['long'] = float(record['long'])
                dicc['lat'] = float(record['lat'])
                dicc['id_arbol'] = int(record['id_arbol'])
                dicc['altura_tot'] = int(record['altura_tot'])
                dicc['diametro'] = int(record['diametro'])
                dicc['inclinacio'] = int(record['inclinacio'])
                dicc['id_especie'] = int(record['id_especie'])
                dicc['nombre_com'] = str(record['nombre_com'])
                dicc['nombre_cie'] = str(record['nombre_cie'])
                dicc['espacio_ve'] =str(record['espacio_ve'])
                dicc['tipo_folla'] =str(record['tipo_folla'])
                dicc['ubicacion'] =str(record['ubicacion'])
                dicc['nombre_fam'] =str(record['nombre_fam'])
                dicc['nombre_gen'] =str(record['nombre_gen'])
                dicc['origen'] = str(record['origen'])
                dicc['coord_x'] = float(record['coord_x'])
                dicc['coord_y'] = float(record['coord_y'])
                lista_arboles.append(dicc)
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}')
        else:
            continue
    return lista_arboles

def especies(lista_arboles):
    especies = ()
    for row in lista_arboles:
        arbol = tuple(str(row['nombre_com']))
        especies += arbol
    especies = set(especies)
    return especies

#Determinar si el programa inicio con argumentos:
#EJemplo de uso:$ python3 arboles.py ../Data/arbolado-en-espacios-verdes.csv
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'

parque = 'GENERAL PAZ'
pprint(leer_parque(nombre_archivo, parque))
lista_arboles = leer_parque(nombre_archivo, parque)

print(f'las especies son del parque {parque} son ', especies(lista_arboles))
