#Ejercicio 1.13 Volumen de una Esfera
#Por Valentin Mengascini
r = float(input("Ingrese el radio de la esfera:"))
print( pow(r, 3) * 4/3 * 3.141592653589793)
'''EL resultado difiere en un numero del dado en la guia
Ingrese el radio de la esfera:6
904.7786842338604
Mientras que en la guia da 904.7786842338603
Una diferencia de 0.0000000000001 de unidad, debido
a que decidi usar pi como un float para ahorrar lineas de codigo
'''
