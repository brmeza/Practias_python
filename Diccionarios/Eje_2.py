# Escribir un programa que pregunte al usuario su nombre, edad, 
# dirección y teléfono y lo guarde en un diccionario. Después 
# debe mostrar por pantalla el mensaje <nombre> tiene <edad> 
# años, vive en <dirección> y su número de teléfono es <teléfono>.

datos={"Nombre":"",
        "Edad":"",
        "Direccion":"",
        "Telefono":""}

print(datos)
nombre=input("ingresar nombre: ")
datos.update({"Nombre":nombre})
edad=input("ingrear edad: ")
datos.update({"Edad":edad})
direccion=input("ingresar direccion: ")
datos.update({"Direccion":direccion})
Telefono=input("ingresar telefono: ")
datos.update({"Telefono":Telefono})

print(f"{datos.get('Nombre')} tiene {datos.get('Edad')} años, vive en {datos.get('Direccion')} y su número de teléfono es {datos.get('Telefono')}.")