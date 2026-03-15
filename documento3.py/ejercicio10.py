def frecuencia_palabras(texto, ignoradas):
    # 1. Limpieza y conversión a lista
    palabras = texto.lower().split()
    frecuencias = {}

    for palabra in palabras:
        # 2. Condicional de omisión (si no está en ignoradas)
        if palabra not in ignoradas:
            # 3. Contar frecuencia en el diccionario
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
                
    return frecuencias

# Ejemplo de uso:
texto_ejemplo = "el gato corre tras el raton y el gato salta"
stop_words = ("el", "y", "tras")
print(frecuencia_palabras(texto_ejemplo, stop_words))
# Salida: {'gato': 2, 'corre': 1, 'raton': 1, 'salta': 1}

"""
usamos .split() para convertir la cadena de texto en una lista de palabras individuales.
primero convertimos el texto a minúsculas y lo dividimos en palabras. Luego, usamos un diccionario para contar la frecuencia de cada palabra, omitiendo aquellas que están en la lista de palabras ignoradas. Finalmente, retornamos el diccionario con las frecuencias.
""" 