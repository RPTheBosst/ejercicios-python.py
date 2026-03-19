

def dispensar_efectivo(monto, tupla_denominaciones):
    desglose = {}
    # Ordenamos las denominaciones de mayor a menor para optimizar el conteo
    denominaciones_ordenadas = sorted(tupla_denominaciones, reverse=True)
    
    saldo_restante = monto
    
    for billete in denominaciones_ordenadas:
        # Bucle y condicional de división: calculamos cuántos billetes de este tipo caben
        if saldo_restante >= billete:
            cantidad = saldo_restante // billete  # División entera
            desglose[billete] = cantidad
            saldo_restante %= billete  # El residuo es lo que falta por entregar
            
    return desglose

# Ejemplo de uso:
denominaciones = (10, 50, 20, 100, 5)
print(dispensar_efectivo(385, denominaciones))
# Salida: {100: 3, 50: 1, 20: 1, 10: 1, 5: 1}

"""
sorted(..., reverse=True): Es fundamental empezar por el billete de mayor valor. Si empezáramos por el de 5, daríamos muchísimos billetes innecesarios.
saldo_restante %= billete: El operador de módulo actualiza lo que nos queda por dispensar. Es como decir: "Ya entregué los billetes de 100, ahora dime cuánto sobra para repartir con los de 50".
"""