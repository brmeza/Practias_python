# Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada 
# vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

datos = {}
new_dato = True
while new_dato:
    clave = input('¿Qué dato quieres introducir? ')
    valor = input(clave + ': ')
    datos[clave] = valor
    print(datos)
    new_dato = input('¿Quieres añadir más información (Si/No)? ') == "Si"
