#Una juguetería tiene mucho éxito en dos de sus productos: 
# payasos y muñecas. Suele hacer venta por correo y la empresa de 
# logística les cobra por peso de cada paquete así que deben calcular 
# el peso de los payasos y muñecas que saldrán en cada paquete a demanda.
# Cada payaso pesa 112 g y cada muñeca 75 g. 
# Escribir un programa que lea el número de payasos y muñecas vendidos 
# en el último pedido y calcule el peso total del paquete que será enviado.

payasos=112
muñecas=75

cant_payasos_vendidos=float(input("cantridad de payasos vendidos: "))
cant_muñecas_vendidas=float(input("cantidad de muñecas vendias: "))

peso_total=(cant_payasos_vendidos*112+cant_muñecas_vendidas*75)/1000

print(f"el peso total es: {peso_total} kg")

