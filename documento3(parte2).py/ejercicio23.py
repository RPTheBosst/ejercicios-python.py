def analizar_caracteres(texto):
    conteos = {}
    
    # Recorremos cada carácter del párrafo
    for char in texto.lower():
        # Condicional: Solo procesamos si es una letra (a-z)
        if char.isalpha():
            if char in conteos:
                conteos[char] += 1
            else:
                conteos[char] = 1
                
    # Convertimos a lista de tuplas y ordenamos alfabéticamente
    resultado_ordenado = sorted(conteos.items())
    
    return resultado_ordenado

# Ejemplo de uso:
parrafo = "¡Hola, mundo! Python es genial."
print(analizar_caracteres(parrafo))
# Salida: [('a', 2), ('e', 2), ('g', 1), ('h', 2), ('l', 2), ...]

"""
char.isalpha(): Este es el if de validación esencial. Devuelve True solo si el carácter es una letra, ignorando automáticamente puntos, comas, signos de exclamación y espacios.
sorted(conteos.items()): El método .items() transforma el diccionario en una lista de tuplas (letra, cantidad). Al aplicar sorted(), Python las ordena alfabéticamente por la letra (el primer elemento de la tupla).
"""