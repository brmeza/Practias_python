#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase= input("ingresar frase: ")
letra= input("ingresar letra: ")
cont=0
for i in range(len(frase)):
    if letra==frase[i]:
        cont+=1
print(cont)