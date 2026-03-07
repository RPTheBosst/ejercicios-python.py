#Calcula precios según si el paquete es nacional o internacional y su peso.
print("Calcula precios según si el paquete es nacional o internacional y su peso.")
print("ingresa si el paquete es nacional (1) o internacional (0): ")
nacional = int(input())
print("ingresa el peso del paquete: ")
peso = float(input())
if nacional == 1:
    if peso <= 5:
        precio = 10
    elif peso > 5 and peso <= 20:
        precio = 20
    else:
        precio = 50
else:
    if peso <= 5:
        precio = 20
    elif peso > 5 and peso <= 20:
        precio = 40
    else:
        precio = 100
print(f"El precio del paquete es: ${precio}")