#Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 
# 16 años y tener unos ingresos iguales o superiores a 1000 €
# mensuales. Escribir un programa que pregunte al usuario su 
# edad y sus ingresos mensuales y muestre por pantalla si el 
# usuario tiene que tributar o no.

edad = int(input("edad: "))
ingresos = float(input("ingresos: "))

if ((edad>16)&(ingresos>=1000)):
    print("toca tributar...")
else:
    print("tas pelao o sin plata")