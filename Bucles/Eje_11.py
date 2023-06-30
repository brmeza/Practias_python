#Escribir un programa que pida al usuario una palabra y luego muestre 
# por pantalla una a una las letras de la palabra introducida empezando
# por la última.

palabre= input("ingresar palabra: ")
for i in range(len(palabre)-1,-1,-1):
    print(palabre[i])