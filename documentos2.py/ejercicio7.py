"""
*⚖️ Ejercicio 7: Comparador de Tres Números*
*📌 Enunciado:* Solicitar al usuario tres números distintos y determinar cuál es el mayor de los tres.
*⚙️ Requerimientos:*
Utilizar operadores lógicos (and, or).
Implementar estructuras if-elif-else.
"""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

if num1 == num2 or num1 == num3 or num2 == num3:
    print("Por favor, ingrese tres números distintos.")
else:
#Determinar cual es el mayor de los tres numeros
    if num1 > num2 and num1 > num3:
        mayor = num1
    elif num2 > num1 and num2 > num3:
        mayor = num2
    else:
        mayor = num3

    print(f"El número mayor es: {mayor}")