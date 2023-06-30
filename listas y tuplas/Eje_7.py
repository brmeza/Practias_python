#Ejercicio 7
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las
# letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
m3=[]
for letra in range(2,len(abc),+3):
    m3.append(abc[letra])
abc=m3
print(abc)
