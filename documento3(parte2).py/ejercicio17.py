def calcular_factoriales(tupla):
    resultados = []
    for num in tupla:
        # Filtramos para ignorar números negativos
        if num >= 0:
            factorial = 1
            # Calculamos el factorial con un bucle
            for i in range(1, num + 1):
                factorial *= i
            # Agregamos el resultado como un diccionario a la lista
            resultados.append({num: factorial})
    return resultados

# Ejemplo de uso
mi_tupla = (3, -2, 5, 0, -1)
print(calcular_factoriales(mi_tupla))
