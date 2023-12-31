#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, 
# correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú: 
# (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
# (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá 
# que hacer lo siguiente:

#Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#Preguntar por el NIF del cliente y mostrar sus datos.
#Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#Terminar el programa.


clientes={}
datos={"nombre":"","direccion":"","telefono":"","correo":"","preferente":""}
eleccion=True
1#añadir cliente
while eleccion:
    eleccion=input("1. Añadir cliente \n2. Eliminar cliente \n3. Mostrar cliente \n4. Listar todos los clientes \n5. Listar clientes preferentes \n6. Terminar \nOpcion: ")
    if eleccion=="1":
        nif=input("ingresar nif: ")
        nombre=input("ingrear nombre: ")
        direccion=input("ingresar direccion")
        telefono=input("ingresar telefono")
        correo=input("ingresar correo")
        preferencia=input("ingresar preferencia")
        datos["nombre"] = nombre
        datos["direccion"] = direccion
        datos["telefono"] = telefono
        datos["correo"] = correo
        datos["preferente"] = preferencia
        clientes[nif]=datos
    if eleccion=="2":
        nif=input("ingresar nif: ")
        clientes.pop(nif)
    if eleccion=="3":
        nif=input("ingresar nif: ")
        if nif in clientes:
            print('NIF:', nif)
            for clave, valor in clientes[nif].items():
                print(clave.title() + ':', valor)
        else:
            print("no esta en lista de clientes...")
    if eleccion=="4":
        print('Lista de clientes')
        for clave, valor in clientes.items():
            print(clave, valor['nombre'])
    if eleccion=="5":
        print('Lista de clientes preferentes')
        for clave, valor in clientes.items():
            if valor['preferente']:
                print(clave, valor['nombre'])
    if eleccion=="6":
        eleccion=False
