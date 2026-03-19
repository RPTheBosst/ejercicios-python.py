def actualizar_tareas(estado_actual, reportes_tupla):
    # Hacemos una copia para no modificar el original directamente
    tareas_nuevas = estado_actual.copy()
    
    for nombre, nuevo_estado in reportes_tupla:
        # if existe tarea: verificamos si la tarea está en nuestro diccionario
        if nombre in tareas_nuevas:
            tareas_nuevas[nombre] = nuevo_estado
            
    return tareas_nuevas

# Ejemplo de uso:
mis_tareas = {"Login": "Pendiente", "Base de datos": "En progreso", "CSS": "Pendiente"}
reporte_del_dia = (("Login", "Completado"), ("API", "Pendiente"), ("CSS", "En progreso"))

resultado = actualizar_tareas(mis_tareas, reporte_del_dia)
print(resultado)
# Salida: {'Login': 'Completado', 'Base de datos': 'En progreso', 'CSS': 'En progreso'}

"""
if nombre in tareas_nuevas: Esta es la condicional de existencia. Si alguien reporta una tarea que no está en la lista oficial (como "API" en el ejemplo), el programa simplemente la ignora.
"""