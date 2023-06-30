# Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será
# el número de factura y el valor el coste de la factura. El programa debe preguntar 
# al usuario si quiere añadir una nueva factura, pagar una existente o terminar. 
# Si desea añadir una nueva factura se preguntará por el número de factura y su coste
# y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número
# de factura y se eliminará del diccionario. Después de cada operación el programa debe 
# mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.

eleccion=True
dict_empresa={}
cantidad_cobrada=0
cantidad_pendiente=0
while eleccion:
    eleccion=input("menu de seleccion: \n1. Añadir nueva factura. \n2. Pagar factura existente. \n3. terminar. \nOpcion=")
    if eleccion=="1":
        print("proceso de añadir factura...")
        numero_de_factura= input("ingresar numero de factura: ")
        coste_de_factura=float(input("ingrsar coste de factura: "))
        dict_empresa[numero_de_factura]=coste_de_factura
        cantidad_pendiente+=coste_de_factura
    elif eleccion=="2":
        print("pagar factura existente...")
        numero_de_factura= input("ingresar numero de factura: ")
        dict_empresa.pop(numero_de_factura)
        cantidad_cobrada+=coste_de_factura
        cantidad_pendiente-=coste_de_factura
    elif eleccion=="3":
        eleccion=False
    print(dict_empresa)
    print("cantidad cobrada: "+str(cantidad_cobrada))
    print("cantidad pendiente: "+str(cantidad_pendiente))

