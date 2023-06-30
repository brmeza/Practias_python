#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo.
#
#1
#3 1
#5 3 1
#7 5 3 1
#9 7 5 3 1
#11 9 7 5 3 1

numero = int(input("ingrese numero: "))

for j in range(numero+1):
    for i in range(j*2-1,0,-2):
        print(i, end=" ")
    print("")