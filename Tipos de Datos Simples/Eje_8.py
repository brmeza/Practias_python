#Escribir un programa que pida al usuario dos números enteros y muestre 
# por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde 
# <n> y <m> son los números introducidos por el usuario, y <c> y <r> son
# el cociente y el resto de la división entera respectivamente.

n=input("ingresar numero 1: ")
m=input("ingresar valor 2: ")

c=float(n)/float(m)
r=int(n)%int(m)

print(round(c))
print(r)
5