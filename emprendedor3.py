import math

P = int(input(f"Calculo de utilidades. \n Ingresar el Precio de Suscripción Normal (la Suscripción Premium tiene un costo 50% mayor): $"))
Pp = P * 1.5
print(f"Suscripción Normal: ${P:.0f} \nSuscripción Premium: ${Pp:.0f}")
Un = int(input(f"¿Cuál es la cantidad de usuarios con Suscripción Normal del último año?: "))
Up = int(input(f"¿Cuál es la cantidad de usuarios con Suscripción Premium del último año?: "))
GT = int(input(f"¿Cuál es el gasto total anual?: $"))

utilidades = (P * Un) + (Pp * Up) - GT

print(f"Las Utilidades del último año es de ${utilidades:.0f}")

ut_past = int(input(f"¿Cuáles fueron las utilidades del año anterior? (el valor ingresado debe ser distinto de 0): $"))

razon = utilidades / ut_past

print(f"La razón de utilidades entre este año y el anterior es de: {razon:.3f}")