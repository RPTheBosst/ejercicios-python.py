"""
Crea un programa que reciba una lista de enteros y extraiga solo los pares.
Requerimientos: Función filtrar_pares(numeros) | Bucle for | Condicional if | Retornar lista de resultados.
"""

def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares   
# Ejemplo de uso

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = filtrar_pares(numeros)
print("Números pares:", resultado)