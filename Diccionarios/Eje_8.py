#Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, 
# y cada par <palabra>:<traducción> separados por comas. El programa debe crear un 
# diccionario con las palabras y sus traducciones. Después pedirá una frase en español
# y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no 
# está en el diccionario debe dejarla sin traducir.

agregar_palabra=True
dicc={}
traduccion=[]
while agregar_palabra:
    palabra_español= input("ingresar palabra en español: ")
    palabra_ingles= input("ingresar palabra en ingles: ")
    dicc[palabra_español]=palabra_ingles
    
    seleccion=input("desea agregar otra palabra... si/no: ")
    if seleccion=="no":
        agregar_palabra=False
        print("ok")

frase=input("ingresar frase: ")
palabras=frase.split(" ")

for i in range(len(palabras)):
    if palabras[i]in dicc:
        traduccion.append(dicc.get(palabras[i]))
    else:
        traduccion.append(palabras[i])

traduccion=" ".join(traduccion)
print(traduccion)
        