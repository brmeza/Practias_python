# Ejercicio 6
# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
# en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
# Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.

asignaturas=["Matematica","quimica","fisica","historia","lenguaje"]
repetir=[]

for i in asignaturas:
    nota= float(input(f"ingresar nota de {i}: "))
    if nota<3:
        repetir.append(i)


print(repetir)
