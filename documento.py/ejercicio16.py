#convertir de 0-100 en letras americanas
numero = int(input("ingresa un numero del 0 al 100: "))
if numero >= 90:
    print("La nota americana es A+")
elif numero >= 80:
    print("La nota americana es A")
elif numero >= 70:
    print("La nota americana es B")
elif numero >= 60:
    print("La nota americana es C")
elif numero >= 50:
    print("La nota americana es D")
elif numero >= 40:
    print("La nota americana es F")
elif numero >= 30:
    print("La nota americana es G")
elif numero >= 20:
    print("La nota americana es H")
elif numero >= 10:
    print("La nota americana es I")
else:
    print("La nota americana es J")