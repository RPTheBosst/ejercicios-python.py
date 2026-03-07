edad = int(input("Por favor, introduce tu edad: "))

if edad <= 0:
    print("La edad no puede ser negativa.")
elif edad <= 12:
    print("Eres un niño.")
elif edad <= 20:
    print("Eres un adolescente.")
elif edad <= 59:
    print("Eres un adulto.")
else:
    print("Eres un anciano.")
