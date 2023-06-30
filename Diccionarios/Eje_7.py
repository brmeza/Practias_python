lista_compras={}
vacio=True
valor_total=0
while vacio:
    articulo=input("ingresar articulo: ")
    precio=int(input("ingresar precio: "))
    
    lista_compras[articulo]=precio
    eleccion=input("desea agregar mas productos si/no....")
    if eleccion=="no":
        vacio=False

for m in lista_compras:
    valor_total=valor_total+lista_compras[m]

print(lista_compras.keys())
print(f"cobro total de la lista: {valor_total}")