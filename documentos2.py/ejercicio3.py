"""
    *🌡️ Ejercicio 3: Conversor de Temperatura*
*📌 Enunciado:* Escriba un programa que convierta una temperatura dada en grados Celsius a Fahrenheit.
*⚙️ Requerimientos:*
Solicitar la entrada por teclado.
Aplicar la fórmula $F = (C \cdot 9/5) + 32$.
Imprimir el resultado con un mensaje explicativo.
    
"""
#La fórmula para convertir de Celsius a Fahrenheit es: F = (C * 9/5) + 32
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} grados Celsius son equivalentes a {fahrenheit} grados Fahrenheit.")
