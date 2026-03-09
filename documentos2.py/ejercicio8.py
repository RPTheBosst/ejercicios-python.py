"""
*🔐 Ejercicio 8: Simulación de Inicio de Sesión*
*📌 Enunciado:* Crear un sistema que simule el acceso a una cuenta. El usuario tiene un máximo de 3 intentos para ingresar la contraseña correcta.
*⚙️ Requerimientos:*
Definir una variable con una contraseña predeterminada.
Utilizar un bucle para controlar los intentos.
Usar la sentencia break si la contraseña es correcta.
Informar si se agotaron los intentos o si el acceso fue concedido.
"""

contraseña_predeterminada = "contraseña123"
intentos = 0
while intentos < 3:
    contraseña_ingresada = input("Ingrese la contraseña: ")
    if contraseña_ingresada == contraseña_predeterminada:
        print("Acceso concedido. Bienvenido")
        break
    else:
        intentos += 1
        print(f"Contraseña incorrecta Intentos {intentos} de 3.")
if intentos == 3:
    print("Has agotado los intentos. Acceso denegado.")
    