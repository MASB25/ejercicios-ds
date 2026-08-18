#!/usr/bin/env python3
def sumaNaturales(numero):
    resultado = 0
    for i in range(0, numero + 1, 1):
        resultado += i
    return resultado

def divTres(numero):
    guardadivisible = []
    for i in range(1, numero + 1, 1):
        resultado = (i % 3)
        if resultado == 0:
            guardadivisible.append(i)
    return guardadivisible

if __name__== "__main__":
    menu = input("Elije 1 para la suma de los primeros N números naturales, 2 para encontrar todos los números divisibles por 3 en un rango dado, o cualquier otro caracter para salir: ")
    match menu:
        case "1":
            while True:
                try:
                    resultado = 0
                    numero = int(input("Ingrese el numero que querias sumar: "))
                    if numero < 0:
                        raise ValueError("Poneme un numero mayor a 0 crack")
                    resultado = sumaNaturales(numero)
                    print(f"El resultado es {resultado}")
                    break
                except ValueError as e:
                    print(f"{e}")
        case "2":
            while True:
                try:
                    resultado = 0
                    numero = int(input("Ingrese el numero que querias dividir: "))
                    if numero <= 0:
                        raise ValueError("Poneme un numero mayor a 0 crack")
                    resultado = divTres(numero)
                    print(f"El/los resultado/s es/son {resultado}")
                    break
                except ValueError as e:
                    print(f"{e}")
        case _:
            print("Que tenga buen dia")
    