# Ejercicio 1
# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
# Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta 
# de la compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los 
# descuentos o el IVA a los productos de la cesta y devolver el precio final de la cesta.

def descuento(precio,desc):
    precio-=precio*desc
    return precio

def aplica_iva(precio,iva):
    precio+=precio*iva
    return precio

def cesta():
    print("")