#Ejercicio 4
# Escribir un programa que pregunte al usuario los números ganadores de la 
# lotería primitiva, los almacene en una lista y los muestre por pantalla 
# ordenados de menor a mayor.

loteria=[]

for i in range(4):
    loteria.append(input("ingresar numero: "))

loteria.sort()
print(loteria)
