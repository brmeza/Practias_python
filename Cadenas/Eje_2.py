#Escribir un programa que pregunte el nombre completo del usuario en la 
# consola y después muestre por pantalla el nombre completo del usuario 
# tres veces, una con todas las letras minúsculas, otra con todas las 
# letras mayúsculas y otra solo con la primera letra del nombre y de los
# apellidos en mayúscula. El usuario puede introducir su nombre combinando
# mayúsculas y minúsculas como quiera.

nombre_completo=input("introducir nombre: ")

nombre_en_min=nombre_completo.lower()
nombre_en_may=nombre_completo.upper()
nombre_prim_may=nombre_en_min.title()

print(nombre_en_min)
print(nombre_en_may)
print(nombre_prim_may)

