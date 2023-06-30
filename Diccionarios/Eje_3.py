# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, 
# pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio 
# de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un 
# mensaje informando de ello.

frutas={"Plátano":1.35,
    "Manzana":0.80,
    "Pera":0.85,
    "Naranja":0.70}

fruta=input("ingresar fruta: ")
kilos=float(input("kilos: "))

if fruta in frutas:
    print(frutas.get(fruta)*kilos)
else:
    print("fruta no disponible")



