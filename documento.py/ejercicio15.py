#ejercicio 15, pide 3 numeros y encuentra el mayor usando IFs anidados

print("ingresa 3 numeros para saber cual es el mayor")
print("ingresa el numero 1")
num1 = int(input("numero 1: "))
print("ingresa el numero 2")
num2 = int(input("numero 2: "))
print("ingresa el numero 1")
num3 = int(input("numero 3: "))

if num1 > num2 :
    if num1 > num3 :
        print(f"Numero {num1} es el mayor")
    else :
        print(f"numero {num3} es el mayor ")
elif num2 > num3 :
    print(f"Numero {num2} es el mayor")
else: 
    print(f"Numero {num3} es el mayor")