def calcular_eleccion(votos):
    conteo = {}
    
    # 1. Procesar cada voto
    for candidato, rol in votos:
        # Definir puntos según el rol
        if rol == "Profesor":
            puntos = 2
        else:
            puntos = 1
            
        # Sumar al diccionario de resultados
        if candidato in conteo:
            conteo[candidato] += puntos
        else:
            conteo[candidato] = puntos
            
    # 2. Encontrar al ganador (máximo puntaje)
    ganador = None
    max_puntos = -1
    
    for candidato, puntos in conteo.items():
        if puntos > max_puntos:
            max_puntos = puntos
            ganador = candidato
            
    return (ganador, max_puntos)

# Ejemplo de uso:
votos_recibidos = [("Ana", "Profesor"), ("Luis", "Alumno"), ("Ana", "Alumno")]
print(calcular_eleccion(votos_recibidos))
# Salida: ('Ana', 3)