#Ejercicio 10
#Escribir un programa que almacene en una lista los siguientes precios, 
# 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios

precios=[50, 75, 46, 22, 80, 65, 8]
precios.sort()
print(f"precio menor: {precios[0]}")
print(f"precio mayor: {precios[-1]}")