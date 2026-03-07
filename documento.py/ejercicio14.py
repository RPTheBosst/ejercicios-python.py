from calendar import monthrange
def dias_en_mes(mes, año):
    return monthrange(año, mes)[1]
print("ingresa el numero del mes para saber cuantos dias tiene:")
mes = int(input())
print(f"El mes {mes} tiene {dias_en_mes(mes, 2020)} días.")