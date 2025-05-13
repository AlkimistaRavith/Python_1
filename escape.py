import math

# 1.1 calculo para velocidad de escape.

planeta = input("Calculemos la velocidad de escape de un planeta. \n Primero, indica el nombre del planeta: ")
r = int(input(f"Ahora debemos conocer su radio (que debe estar redondeado en Kilómetros). \n ¿Cuál es el radio de {planeta} en [Km]?: "))
g = float(input(f"Por último necesitamos la constante gravitatoria de {planeta}, indicada en [m/s^2] (recuerda que este valor no puede ser negativo, ni 0) \n ¿Cual es la constante g del planeta?: "))
rm = r*1000

Ve = math.sqrt(2*g*rm)

print(f"Con un radio de {r} [Km], y una constante g de {g} [m/s^2]. \n El planeta {planeta} tiene una Velocidad de escape de: {Ve:.3f} [m/s]")

