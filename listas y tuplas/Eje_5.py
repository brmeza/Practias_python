# Ejercicio 5
# Escribir un programa que almacene en una lista los números del 1 al 10 
# y los muestre por pantalla en orden inverso separados por comas.

num=[1,2,3,4,5,6,7,8,9,10]

for i in range(len(num),0,-1):
    print(f"{i},", end=" ")