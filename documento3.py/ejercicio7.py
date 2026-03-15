def revisar_inventario(productos):
    reabastecer = {}
    for id_prod, nombre, cantidad in productos:
        if cantidad < 10:
            reabastecer[id_prod] = nombre
    return reabastecer

# Ejemplo de uso:
inventario = [
    (101, "Manzanas", 25),
    (102, "Leche", 5),
    (103, "Pan", 8)
]

print(revisar_inventario(inventario))
# Salida: {102: 'Leche', 103: 'Pan'}