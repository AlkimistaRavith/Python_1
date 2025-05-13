import math

#Parte 2.3, considerando solo la fórmula original (utilidades = P * U - GT)

P = float(input(f"Calculo de utilidades. \n Ingresar el Precio de suscripción: $"))
U = int(input(f"¿Cuál es la cantidad total de usuarios del último mes?: "))
GT = int(input(f"¿Cuál es el gasto total mensual?: $"))

utilidades = P * U - GT

print(f"Las Utilidades del último mes es de ${utilidades:.0f}")

ut_past = int(input(f"¿Cuáles fueron las utilidades del año anterior? (el valor ingresado debe ser distinto de 0): $"))

razon = utilidades / ut_past

print(f"La razón de utilidades entre este año y el anterior es de: {razon:.3f}")
