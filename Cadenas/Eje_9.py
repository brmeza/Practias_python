#Escribir un programa que pregunte al usuario la fecha de su nacimiento
# en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.
# Adaptar el programa anterior para que también funcione cuando el día o
# el mes se introduzcan con un solo carácter.

fecha=input("ingresar fecha de nacimineto fomrato dd/mm/aaaa: ")

dia=fecha[:fecha.find("/")]
mesaño=fecha[fecha.find("/")+1:]
mes=mesaño[:fecha.find("/")]
año=fecha[-4:]

print("DIA",dia)
print("MES",mes)
print("AÑO",año)
