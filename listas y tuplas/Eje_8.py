
palabra=input("ingresar palabra: ")
rev_palabra=list(palabra)
palabra=list(palabra)
rev_palabra.reverse()
print(palabra)
print(rev_palabra)
if palabra==rev_palabra:
    print("es un palindromo")
else:
    print("no es palindromo")

