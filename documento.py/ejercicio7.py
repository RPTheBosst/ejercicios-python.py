# pide a y b e intercambia sus valores usando una 3 variable

print("ingresa a y b")
a = input("a -> ")
b = input("b -> ")
print("ingresa c para cambiar los valores")
c = input("c -> ")

if c == "1" :
    a,b = b,a
    print(f"a = {a}")
    print(f"b = {b}")
else:
    print("no se pueden invertil los valores")