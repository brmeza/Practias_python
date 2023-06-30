#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 
# 4% de interés al año. Estos ahorros debido a intereses, que no se cobran
# hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. 
# Escribir un programa que comience leyendo la cantidad de dinero depositada 
# en la cuenta de ahorros, introducida por el usuario. Después el programa 
# debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, 
# segundo y tercer años. Redondear cada cantidad a dos decimales.

cant_dinero_dep= float(input("cantidad de dinero depocitado: "))

primer_ano=cant_dinero_dep*(1+0.04)
segundo_ano=primer_ano*(1+0.04)
tercer_ano=segundo_ano*(1+0.04)

print(f"año uno: {round(primer_ano,2)}")
print(f"año dos: {round(segundo_ano,2)}")
print(f"año tres: {round(tercer_ano,2)}")
