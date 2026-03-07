usuario = input("Por favor, introduce tu nombre de usuario: ")
contraseña = input("Por favor, introduce tu contraseña: ")

if usuario == "admin" and contraseña == "1234":
    print("Acceso concedido, puede pasar admin.")
else:
    print("Acceso denegado, no puede pasar.")