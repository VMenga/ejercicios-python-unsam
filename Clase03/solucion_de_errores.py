#solucion_de_errores.py
#Por Valentin Mengascini
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error en este codigo fue el uso de 'return', el cual
#sale de la funcion una vez devuelto el valor. Se elimina el 'else' y se
#coloca al final un return False
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: Faltaban los ':' al final de def, while e if. Tambien el doble
# '=' que indica "es igual a" en el if. Y se corrige el 'Falso' a 'False'
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: Esta funcion solo detecta '1' en forma de string y no en forma
# de numero integral. Agregue expresion = str(expresion) para asegurar que
#la expresion que se esta probando sea un string.
def tiene_uno(expresion):
    expresion = str(expresion)
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%
#Ejercicio 3.4. Función tiene_uno()
#Comentario:

#%%
#Ejercicio 3.5. Función tiene_uno()
#Comentario:
