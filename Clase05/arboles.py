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

#Hace un set de las especies segun el parque indicado
def especies(lista_arboles):
    especies = ()
    for n_fila, fila in enumerate(lista_arboles, start=1):
        arbol = (fila['nombre_com'],)
        especies = especies + arbol
    especies = set(especies)
    return especies

#Determinar si el programa inicio con argumentos:
#EJemplo de uso:$ python3 arboles.py ../Data/arbolado-en-espacios-verdes.csv
if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/arbolado-en-espacios-verdes.csv'

#Define el parque e imprime la lista de diccionarios
parque = 'GENERAL PAZ'
pprint(leer_parque(nombre_archivo, parque))
lista_arboles = leer_parque(nombre_archivo, parque)

#Imprime la lista de especies
print(f'Las especies son del parque {parque} son ', especies(lista_arboles))


'''
Salida de prueba:  python3 arboles.py '../Data/arbolado-en-espacios-verdes.csv'
{'altura_tot': 10,
  'coord_x': 96001.202845,
  'coord_y': 107091.71175399999,
  'diametro': 35,
  'espacio_ve': 'GENERAL PAZ',
  'id_arbol': 51729,
  'id_especie': 342,
  'inclinacio': 0,
  'lat': -34.5653342811,
  'long': -58.5068743702,
  'nombre_cie': 'Cupressus sp.',
  'nombre_com': 'Ciprés',
  'nombre_fam': 'Cupresáceas',
  'nombre_gen': 'Cupressus',
  'origen': 'Exótico',
  'tipo_folla': 'Árbol Conífero Perenne',
  'ubicacion': 'LARRALDE, CRISOLOGO, AV. - PAZ, GRAL., AV.- AIZPURUA'}]

 Las especies son del parque GENERAL PAZ son  {'Palma de california', 'Washingtonia (Palmera washingtonia)', 'Caqui', 'Fenix', 'Ciprés blanco', 'Ciprés calvo', 'Washingtonia', 'Timbó (Oreja de negro)', 'Ceibo', 'Palmito', 'Ficus', 'Cedro', 'Tuya oriental', 'Tipa blanca', 'No Determinado', 'No Determinable', 'Morera de papel (Moral de China)', 'Jacarandá', 'Chamaecyparis', 'Roble común', 'Níspero japonés', 'Plátano', 'Fresno americano', 'Cedrela', 'Sauce eléctrico', 'Morera negra', 'Acacia negra', 'Cedro del Atlas (Cedro plateado o Cedro atlántico)', 'Arce negundo', 'Álamo negro', 'Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert)', 'Casuarina', 'Visco (Viscote, Arca)', 'Liquidambar', 'Cedro del Himalaya variedad aurea', 'Magnolia', 'Alcanforero', 'Juniperus', 'Ligustro disciplinado (Ligustro variegado)', 'Olmo', 'Fresno (Fresno común)', 'Eucalipto', 'Pino carrasco (Pino de Jerusalén)', 'Cedro de San Juan', 'Libocedro (Calocedro)', 'Árbol del cielo (Ailanto o Árbol de los dioses)', 'Álamo blanco piramidal', 'Bunya-bunya (Araucaria de Bidwill)', 'Roble sedoso (Grevillea)', 'Ciprés', 'Corona de cristo', 'Olmo europeo', 'Laurus', 'Palma Bangalow  (Palma Rey)', 'Ciprés leylandi', 'Paraíso', 'Tilo', 'Roble americano', 'Laurel de jardin (Laurel de flor)', 'Criptomeria (Cedro del Japón)', 'Limpiatubos', 'Tuja', 'Ombú', 'Roble', 'Palo borracho rosado', 'Nogal europeo (Nogal común)', 'Pino', 'Acacia blanca', 'Pindó', 'Cedro del Himalaya', 'Pino del Paraná (Pino de Misiones o Pino de Brasil)', 'Olivo', 'Fotinia', 'Olea', 'Falso Guayabo (Guayaba del Brasil)', 'Morera blanca', 'Ginkgo', 'Pino de las canarias', 'Olivo oloroso', 'Ligustro', 'Lapacho rosado'}


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
