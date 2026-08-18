#!/usr/bin/env python3
if __name__ == "__main__":
    booleano = True
    while booleano:
        contraseña = input("Ingresa una contraseña: ")
        if len(contraseña) < 8:
            print("Muy corta maestro")
        elif contraseña.isupper():
            print("Te comiste la mayuscula mi rey")
        elif contraseña.islower():
            print("Te comiste la minuscula mi rey")
        else:
            print("Te juro que no vi tu constraseña, pero confio")
            booleano = False
            cantidad = 0
    while cantidad < 3:
        try:
            repeticion = input("A ver si te acordas tu contraseña, escribila: ")
            if repeticion == contraseña:
                print("Sos crack")
                cantidad = 4
            else:
                print("Mepa que esa no era, floja esa memoria...")
                cantidad += 1
            if cantidad == 3:
                raise ValueError("Te pasaste de intentos, a laburar esa memoria")
            
        except ValueError as e:
            print(f"{e}")


    
    
