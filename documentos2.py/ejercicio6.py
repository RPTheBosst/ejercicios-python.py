"""
*📈 Ejercicio 6: Contador de Números Positivos*
*📌 Enunciado:* El programa debe pedir números al usuario de forma indefinida hasta que este ingrese un número negativo.
*⚙️ Requerimientos:*
Utilizar un bucle while.
Llevar un conteo de cuántos números positivos fueron ingresados antes del negativo.
No usar estructuras de datos (listas/arreglos).
"""

cantidad_positivos = 0

#Pedimos el primer número antes de entrar al bucle
numero = int(input("Ingresa un número (negativo para salir): "))

#Bucle: se ejecuta mientras el número sea 0 o mayor
while numero >= 0:
    cantidad_positivos += 1 
    numero = int(input("Ingresa otro número: "))

#Resultado final
print(f"Ingresaste {cantidad_positivos} números positivos.")
