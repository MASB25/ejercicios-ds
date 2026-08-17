#!/usr/bin/env python3
def farACels(valorF):
    resultado = ((valorF - 32) * 5/9)
    return resultado

def celsAFar(valorC):
    resultado = ((valorC *9/5) + 32)
    return resultado
if __name__ ==  "__main__":
    while True:
        try:
            valor = float(input("Seleccione un valor a convertir: "))
            break
        except ValueError:
            print("Le pifiaste al numero maquina")
    escala = input("Seleccione un C si el valor es celsius o F si es fahrenheit: ").strip().upper()

    if escala == 'C':
        result= celsAFar(valor)
        print(f"La conversion es {result}")

    elif escala == 'F':
        result= farACels(valor)
        print(f"La conversion es {result}")

    else:
        print(f"La escala ingresada no esta en el rango permitido")



