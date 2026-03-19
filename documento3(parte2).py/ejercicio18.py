def validar_contrasenas(lista):
    validas = []
    invalidas = []
    
    for password in lista:
        # Regla 1: Longitud > 8 | Regla 2: Contiene al menos un número
        tiene_numero = any(char.isdigit() for char in password)
        
        if len(password) > 8 and tiene_numero:
            validas.append(password)
        else:
            invalidas.append(password)
            
    # Retornamos el diccionario convirtiendo las listas en tuplas
    return {
        "validas": tuple(validas),
        "invalidas": tuple(invalidas)
    }

# Ejemplo de uso:
passwords = ["12345", "python2024", "segura123", "clave", "solonumeros1"]
print(validar_contrasenas(passwords))