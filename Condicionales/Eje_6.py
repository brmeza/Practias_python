#Ejercicio 6
#Los alumnos de un curso se han dividido en dos grupos A y B 
# de acuerdo al sexo y el nombre. El grupo A esta formado por
# las mujeres con un nombre anterior a la M y los hombres con
# un nombre posterior a la N y el grupo B por el resto. Escribi
# un programa que pregunte al usuario su nombre y sexo, y 
# muestre por pantalla el grupo que le corresponde.

nombre=str(input("nombre: "))
sexo=str(input("sexo: "))

grupo_A= ["a","b","c","d","e","f","j","h","i","j","k","l","m"]
grupo_B=["n","o","p","q","r","s","t","u","v","w","x","y","z"]

if ((sexo=="f")& (nombre[0].lower() in grupo_A))|((sexo=="m")& (nombre[0].lower() in grupo_B)):
    print("ERES GRUPO A")
else:
    print("ERES GRUPO B")