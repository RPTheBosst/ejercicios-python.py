"""
*❗ Ejercicio 10: Cálculo de Factorial*
*📌 Enunciado:* Solicitar un número entero positivo y calcular su factorial ($n!$).
*⚙️ Requerimientos:*
Utilizar un bucle (ya sea for o while).
Validar que el número ingresado no sea negativo mediante un condicional.
Mostrar el resultado final por pantalla.
"""

numero = int(input("Ingrese un número entero positivo para calcular su factorial: "))
if numero < 0:
    print("Error: El número debe ser positivo.")
else:
    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print(f"El factorial de {numero} es: {factorial}")
    