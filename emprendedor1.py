import math

#Parte 2.1, considerando primer calculo de utilidades.

P = float(input(f"Calculo de utilidades. \n Ingresar el Precio de suscripción: $"))
U = int(input(f"¿Cuál es la cantidad total de usuarios del último mes?: "))
GT = int(input(f"¿Cuál es el gasto total mensual?: $"))

utilidades = P * U - GT

print(f"Las Utilidades del último mes es de ${utilidades:.0f}")
