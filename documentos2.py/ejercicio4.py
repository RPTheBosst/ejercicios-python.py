"""
*✖️ Ejercicio 4: Tabla de Multiplicar*
*📌 Enunciado:* Generar la tabla de multiplicar de un número ingresado por el usuario, del 1 al 10.
*⚙️ Requerimientos:*
Utilizar un bucle for.
Imprimir cada línea con el formato: "n x i = resultado".
"""

numero = int(input("Ingrese un número para generar su tabla de multiplicar: "))
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")