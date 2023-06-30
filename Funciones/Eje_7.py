# Ejercicio 7
# Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def calc_cuadrado(lista):
    cuadrados=[]
    for i in range(len(lista)):
        calc=lista[i]*lista[i]
        cuadrados.append(calc)
    return cuadrados
print(calc_cuadrado([1,2,3,4]))