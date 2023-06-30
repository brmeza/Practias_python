# Ejercicio 6
# Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def calc_media(media):
    total = sum(media)
    media=total/len(media)
    return media

print(calc_media([1,2,3,4,5,54]))

