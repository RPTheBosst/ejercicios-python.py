def encontrar_maximo(secuencia):
    if not secuencia:
        return None
    
    maximo = secuencia[0]
    for numero in secuencia:
        if numero > maximo:
            maximo = numero
    return maximo

# Ejemplo de uso:
numeros = [10, 45, 2, 87, 33]
print(encontrar_maximo(numeros))  # Salida: 87