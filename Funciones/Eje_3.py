# Ejercicio 3
# Escribir una función que reciba un número entero positivo y devuelva su factorial.
num=0

def factorial (num):
    total=1
    for i in range(num):
        total*=i+1
    return total

print(factorial(5))
