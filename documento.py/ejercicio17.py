#¿Es Equilátero, Isósceles o Escaleno? Evalúa sus 3 lados.

print("ingresa los 3 lados de un triangulo para saber si es equilatero, isosceles o escaleno")

a = float(input("lado a: "))
b = float(input("lado b: "))    
c = float(input("lado c: "))
if a == b == c:
    print("El triangulo es equilatero")
elif a == b or b == c or a == c:
    print("El triangulo es isosceles")
else:    
    print("El triangulo es escaleno")