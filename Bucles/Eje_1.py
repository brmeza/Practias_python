#Ejercicio 1
#Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra = input("ingrese la palabra a repetir las 10: ")
i=1

print("manera uno.. for...")
for a in range(10):
    print(palabra)

print("manera 2... while...")
while i<=10:
    print(palabra)
    i+=1
    


