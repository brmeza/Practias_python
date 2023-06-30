# Ejercicio 8
# Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.

def estadisticas(lista):
    n = len(lista)
    media = sum(lista) / n
    varianza = sum((x - media) ** 2 for x in lista) / n
    desv_tipica = varianza ** 0.5
    return {'media': media, 'varianza': varianza, 'desv_tipica': desv_tipica}

datos = [1, 2, 3, 4, 5]
resultado = estadisticas(datos)
print(resultado) 