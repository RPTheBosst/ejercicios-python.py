def invertir_selectivo(palabras):
    resultado = {}
    for p in palabras:
        if len(p) > 4:
            resultado[p] = p[::-1]
    return resultado

# Ejemplo de uso:
lista = ["hola", "python", "sol", "mundo", "programar"]
print(invertir_selectivo(lista)) 

"""
p[::-1]: Es un truco de Python llamado slicing que recorre la cadena de atrás hacia adelante, invirtiéndola fácilmente.
resultado[p] = ...: Agregamos la palabra original como clave y la invertida como valor.
"""