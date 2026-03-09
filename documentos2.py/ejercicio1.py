""""
*📝 Ejercicio 1: Calculadora de Promedio de Notas*
*📌 Enunciado:* Desarrolle un programa que solicite al usuario tres notas de un examen y determine si el estudiante aprobó o reprobó.
*⚙️ Requerimientos:*
Utilizar variables de tipo flotante (float).
Calcular el promedio aritmético.
Usar una estructura condicional para imprimir "Aprobado" si el promedio es mayor o igual a 60, de lo contrario imprimir "Reprobado".
"""

nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))   

promedio = (nota1 + nota2 + nota3) / 3

if promedio >= 60:
    print("felicidades! Has aprobado el curso.")
else:
    print("no lograste cumplir las exigencias del curso. Reprobado")