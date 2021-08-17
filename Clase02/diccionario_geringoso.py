#Ejercicio 2.14 Geringoso
#Por Valentin Mengascini & Heinz Doofenshmirtz

def geringoseador(palabra): #Funcion para traducir la palabra
    final = ""
    for letra in palabra:
        if letra in "AEIOUaeiou":
            final += letra + "p" + letra
        else :
            final += letra
    return final

#Esta parte itinera sobre los elementos de la lista
diccionario = {}
lista = ['banana', 'manzana', 'mandarina']
for palabra in lista:
    diccionario[palabra] = geringoseador(palabra)
print(diccionario)

'''
Salida de prueba:
python3 diccionario_geringoso.py
{'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}
'''
