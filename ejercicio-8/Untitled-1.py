
def calcular_precio_final(precio_base, porcentaje_descuento=10, es_vip=False):
    total = precio_base - (precio_base * (porcentaje_descuento/100))
    if es_vip == True:
        total -= (total * (5/100))

    return total
valido = True
while valido:
    try:
        base = float(input("Ingrese precio base: "))
        if(base < 0):
            raise ValueError("Muy bajo el precio, maestro")
        descuento = float(input("Ingrese descuento: "))
        if(descuento < 0):
            raise ValueError("No le bajaste nada al precio, crack")
        entrada_vip = input("Ingrese True si es vip, de lo contrario ingrese otra cosa: ")
        vip = (entrada_vip.lower() == "true")
        valido = False
    except ValueError as e:
        print(f"{e}")
paraTestear = calcular_precio_final(base, descuento, vip)
print(f"El precio final del sujeto es de ${paraTestear}")





