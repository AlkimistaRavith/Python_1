import math

P = float(input(f"Calculo de utilidades. \n Ingresar el Precio de Suscripción Normal (la Suscripción Premium tiene un costo 50% mayor): $"))
print(f"Suscripción Normal: ${P} \nSuscripción Premium: ${P*1.5}")
Un = int(input(f"¿Cuál es la cantidad de usuarios con Suscripción Normal del último año?: "))
Up = int(input(f"¿Cuál es la cantidad de usuarios con Suscripción Premium del último año?: "))
GT = int(input(f"¿Cuál es el gasto total anual?: $"))

utilidades = (P * Un) + (P * 1.5 *Up) - GT

print(f"Las Utilidades del último año es de ${utilidades:.0f}")
