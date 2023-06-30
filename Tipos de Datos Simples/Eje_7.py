#Escribir un programa que pida al usuario su peso (en kg) y estatura 
# (en metros), calcule el índice de masa corporal y lo almacene en una 
# variable, y muestre por pantalla la frase Tu índice de masa corporal 
# es <imc> donde <imc> es el índice de masa corporal calculado 
# redondeado con dos decimales.

peso=float(input("ingresar tu peso en kg: "))
estatura=float(input("ingresa tu estatura en m: "))

indice_masa_corp=round((peso/(estatura)**2),2)#round permite redondear a solo 2 decimales

print(indice_masa_corp)