# Si gastas más de $100, ¡tienes un 15% de descuento!

precio = int(input("ingrese el precio de su producto: "))

descuento = precio * 0.15

total_a_pagar = precio - descuento

num1 = 100

if  precio >= num1:
    print(f"debera pagar un total de ${total_a_pagar:.2f}")
else:
    print(f"debera pagar un total de ${precio}")