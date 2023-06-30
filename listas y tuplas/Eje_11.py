#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2)
# en dos listas y muestre por pantalla su producto escalar.

u=[1,2,3]
v=[-1,0,2]
u_v=0
for i in range(len(u)):
    u_v=u_v+u[i]*v[i]
print(u_v)