#Una panadería vende barras de pan a 3.49€ cada una. 
# El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas 
# que no son del día. Después el programa debe mostrar el precio habitual 
# de una barra de pan, el descuento que se le hace por no ser fresca y el 
# coste final total.
precio_barra_de_pan=3.49
descuento=0.6

barras_vendidad=float(input("barras vendidas: "))

barra_fresca=barras_vendidad*3.49
barras_no_frescas=((barras_vendidad*3.49)-barra_fresca*descuento)

print(f"si el pan es fresco cobrar {round(barra_fresca,2)} Euros")
print(f"si el pan no es fresco cobrar {round(barras_no_frescas,2)} Euros")