"""
* Ejercicio 5: Sumatoria con Límite*
* Enunciado:* Realizar un programa que sume números enteros consecutivos empezando desde 1 hasta que la suma total alcance o supere un valor límite ingresado por el usuario.
* Requerimientos:*
Utilizar un bucle while.
Imprimir el total de la suma y cuántos números se necesitaron.
"""

limite = int(input("Ingresa el valor límite: "))
suma = 0
contador = 0

while suma < limite:
    contador += 1
    suma += contador

print(f"Suma total: {suma}")
print(f"Números sumados: {contador}")