def cifrar_mensajes(lista_diccs):
    cifrados = []
    
    for item in lista_diccs:
        mensaje = item["mensaje"]
        prioridad = item["prioridad"]
        
        # if prioridad: Definimos el salto (3 para alta, 1 para baja)
        salto = 3 if prioridad == "alta" else 1
        
        # Bucle interno para cifrar caracteres
        mensaje_cifrado = ""
        for char in mensaje:
            if char.isalpha():
                # Desplazamos el carácter en el código ASCII
                nuevo_char = chr(ord(char) + salto)
                mensaje_cifrado += nuevo_char
            else:
                mensaje_cifrado += char
        
        # Guardamos el nuevo diccionario con el mensaje alterado
        cifrados.append({"mensaje": mensaje_cifrado, "prioridad": prioridad})
            
    return tuple(cifrados)

# Ejemplo de uso:
datos = [
    {"mensaje": "hola", "prioridad": "alta"},
    {"mensaje": "abc", "prioridad": "baja"}
]
print(cifrar_mensajes(datos))
# Salida: ({'mensaje': 'knod', 'prioridad': 'alta'}, {'mensaje': 'bcd', 'prioridad': 'baja'})

"""
ord(char) + salto: La función ord() obtiene el valor numérico de la letra. Le sumamos el desplazamiento y luego chr() lo convierte de nuevo a la nueva letra.
if char.isalpha(): Esta validación asegura que solo cifremos letras, dejando espacios o puntos tal como están para no romper el mensaje.
"""