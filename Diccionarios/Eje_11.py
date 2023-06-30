# El directorio de los clientes de una empresa está organizado en una cadena de 
# texto como la de más abajo, donde cada línea contiene la información del nombre,
# email, teléfono, nif, y el descuento que se le aplica. Las líneas se separan con 
# el carácter de cambio de línea \n y la primera línea contiene los nombres de los 
# campos con la información contenida en el directorio.

cadena = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"

directorio = {}

cadena = cadena.split("\n")
datos = cadena[0].split(";")

for i in range(1,len(cadena)):
    nif = cadena[i].split(";")[0]
    subdic = {}
    for j in range(1,len(datos)):
        subdatos = cadena[i].split(";")
        subdic[datos[j]] = subdatos[j]
    directorio[nif] = subdic

print(directorio)