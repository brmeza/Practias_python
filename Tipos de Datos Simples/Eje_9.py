#Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión.

invercio=float(input("cuanto va a invertir: "))
interes=float(input("interes anual: "))
años=float(input("numero de años: "))

capital=(round(invercio*(interes/100+1)**años,2))
print(capital)