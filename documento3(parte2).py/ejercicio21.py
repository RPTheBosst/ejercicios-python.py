def buscar_contactos(agenda_dicc, inicial):
    resultados = []
    
    for nombre, datos in agenda_dicc.items():
        # Regla 1: Que empiece por la inicial (ignorando mayúsculas/minúsculas)
        # Regla 2: Que la clave "telefono" exista en el sub-diccionario
        if nombre.lower().startswith(inicial.lower()) and "telefono" in datos:
            # Guardamos como tupla (Nombre, Telefono)
            resultados.append((nombre, datos["telefono"]))
            
    return resultados

# Ejemplo de uso:
mi_agenda = {
    "Ana": {"telefono": "123-456", "email": "ana@mail.com"},
    "Alberto": {"email": "al@mail.com"}, # Sin teléfono
    "Beatriz": {"telefono": "987-654"},
    "antonio": {"telefono": "555-000"}
}

print(buscar_contactos(mi_agenda, "A"))
# Salida: [('Ana', '123-456'), ('antonio', '555-000')]

"""
"telefono" in datos: Esta condicional de existencia evita que el programa falle si un contacto tiene correo pero no número telefónico.
agenda_dicc.items(): Usamos este método en el bucle para obtener tanto el nombre (clave) como los datos (que es otro diccionario con teléfono, email, etc.).
"""