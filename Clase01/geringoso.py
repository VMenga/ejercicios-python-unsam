#Ejercicio 1.18 Geringoso
#Por Valentin Mengascini
final=""
palabra = input("Inserte palabra a traducir:")
for letra in palabra:
    if letra in "AEIOUaeiou":
        final += letra
        final += "p"
        final += letra
    else :
        final += letra
print(final)
