def encontrar_duplicados(ids):
    conteos = {}
    
    # Primer bucle: Contar ocurrencias
    for i in ids:
        if i in conteos:
            conteos[i] += 1
        else:
            conteos[i] = 1
            
    # Segundo bucle: Filtrar solo los repetidos y dar formato
    repetidos = {}
    for id_unico, cantidad in conteos.items():
        if cantidad > 1:
            repetidos[id_unico] = (cantidad,)
            
    return repetidos

# Ejemplo de uso:
mis_ids = [101, 102, 101, 103, 102, 101, 104]
print(encontrar_duplicados(mis_ids))
# Salida: {101: (3,), 102: (2,)}
"""
if i in conteos: esta condicional de conteo verifica si el ID ya ha aparecido antes. Si ya está, sumamos 1; si no, lo iniciamos en 1.
"""