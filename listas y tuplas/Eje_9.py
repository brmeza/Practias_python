#Ejercicio 9
#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal.

vocales=["a","e","i","o","u"]
palabra=list(input("ingresar palabra: "))

for i in vocales:
    print(f"la vocal {i} esta {palabra.count(i)} veces")