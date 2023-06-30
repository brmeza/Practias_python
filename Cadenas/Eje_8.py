#Escribir un programa que pregunte por consola el precio de un producto 
# en euros con dos decimales y muestre por pantalla el número de euros 
# y el número de céntimos del precio introducido.

precio=input("precio del producto en Euros con dos decimales: ")

print(precio[:precio.find(".")],' Euros y',precio[precio.find('.')+1:],"centimos")

