"""
*🔄 Ejercicio 9: Generador de Secuencia Numérica Especial*
*📌 Enunciado:* Imprimir todos los números del 1 al 50, pero con las siguientes condiciones: si el número es divisible por 3 imprimir "Fizz", si es divisible por 5 imprimir "Buzz", y si es divisible por ambos imprimir "FizzBuzz".
*⚙️ Requerimientos:*
Utilizar un bucle for con el método range().
Uso estricto de condicionales anidados o múltiples.
Uso de operadores de comparación y módulo.
"""

for numero in range(1, 51):
    if numero % 3 == 0 and numero % 5 == 0:
        print("FizzBuzz")
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
