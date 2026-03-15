def contar_vocales(texto):
    contador = 0
    vocales = "aeiouAEIOU"
    for caracter in texto:
        if caracter in vocales:
            contador += 1
    return contador

# Ejemplo de uso:
frase = "Hola Mundo"
print(contar_vocales(frase))  # Salida: 4