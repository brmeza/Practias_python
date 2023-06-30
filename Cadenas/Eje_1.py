#Escribir un programa que pregunte el nombre del usuario en la consola 
# y un número entero e imprima por pantalla en líneas distintas el nombre
# del usuario tantas veces como el número introducido.

nombre=input("nombre: ")
cant=int(input("cantidad de veces a imprimir"))
num=1
while num<=cant:
    print(nombre)
    num=num+1
    

