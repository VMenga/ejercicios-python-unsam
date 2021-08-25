#arboles.py
#Por Valentin Mengascini
import csv

def leer_parque(nombre_archivo):
    arboles = []
    f = csv.reader(open(nombre_archivo, 'rt'), delimiter=',')
    encabezados = next(f)
    for n_fila, fila in enumerate(f, start=1):
        record = dict(zip(encabezados, fila))
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
            dicc['tipo_folla'] =str(record['tipo_folla'])
            dicc['espacio_ve'] =str(record['espacio_ve'])
            dicc['ubicacion'] =str(record['ubicacion'])
            dicc['nombre_fam'] =str(record['nombre_fam'])
            dicc['nombre_gen'] =str(record['nombre_gen'])
            dicc['origen'] = str(record['origen'])
            dicc['coord_x'] = float(record['coord_x'])
            dicc['coord_y'] = float(record['coord_y'])
            arboles.append(dicc)
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
    return arboles

print(leer_parque('../Data/arbolado-en-espacios-verdes.csv'))