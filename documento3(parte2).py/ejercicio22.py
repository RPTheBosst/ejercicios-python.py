def procesar_reservas(disponibilidad, solicitudes_tupla):
    confirmados = []
    en_espera = []
    asientos_libres = disponibilidad
    
    for reserva in solicitudes_tupla:
        # reserva[0] es el nombre, reserva[1] es la cantidad de asientos
        nombre, cantidad = reserva
        
        # if hay cupo: verificamos si quedan suficientes asientos
        if asientos_libres >= cantidad:
            asientos_libres -= cantidad  # Restamos de la disponibilidad
            confirmados.append(nombre)
        else:
            en_espera.append(nombre)
            
    return {
        "confirmados": confirmados,
        "en_espera": en_espera
    }

# Ejemplo de uso:
cupo_inicial = 10
pedidos = (("Juan", 4), ("Marta", 7), ("Pedro", 2))
print(procesar_reservas(cupo_inicial, pedidos))
# Salida: {'confirmados': ['Juan', 'Pedro'], 'en_espera': ['Marta']}

"""
if asientos_libres >= cantidad: Esta es la condicional de cupo. Si el número de asientos que pide la persona es menor o igual a lo que queda, la reserva procede
"""